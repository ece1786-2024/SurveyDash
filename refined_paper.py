import time
import re
import os
import pymupdf4llm
import tiktoken
from openai import OpenAI

from prompts import (
    _outline_generation_prompt,
    _outline_revision_prompt,
    _outline_advice_prompt,
    _section_outline_prompt,
    _section_writer_prompt,
    _section_refine_prompt,
    _combined_section_suggestion_prompt,
    _check_hallucination_prompt,
    _gen_summarization_prompt,
)

# to be revoked
client = OpenAI(
    api_key='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'
)


def make_chat_request(client, messages, model="gpt-4o", temperature=0.3, top_p=0.5) -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            top_p=top_p
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error in OpenAI API call: {e}")


def write_to_file(filepath, content):
    file_name = os.path.basename(filepath)
    directory = os.path.dirname(filepath)
    if not directory:
        directory = "."

    try:
        with open(f'{directory}/{int(time.time())}_{file_name}', 'w') as f:
            f.write(content)
        with open(filepath, 'w') as f:
            f.write(content)
    except IOError as e:
        raise Exception(f"Error writing to file {filepath}: {e}")


def extract_section_titles(recent_advice):
    pattern = r"### (\d+\.\s+[A-Za-z -]+)"
    matches = re.findall(pattern, recent_advice)
    section_titles = [re.sub(r"\d+\.\s+", "", title).strip() for title in matches]
    return section_titles


def gen_survey_outline(abstracts, topic):
    outline_generation_prompt_pt_1 = "\n".join(_outline_generation_prompt.format(topic=topic).split("\n")[2:])
    outline_generation_msg = [
        {
            "role": "system",
            "content": _outline_generation_prompt.format(topic=topic)
        },
        {
            "role": "user",
            "content": abstracts
        }
    ]
    # Step 1 - Generating initial outline
    print("Generating initial outline...")
    init_outline = make_chat_request(client, outline_generation_msg)
    write_to_file("init_outline.txt", init_outline)
    outline_revision_msg = [
        {
            "role": "system",
            "content": _outline_revision_prompt.format(
                prev_prompt=outline_generation_prompt_pt_1,
                reply=init_outline
            )
        }
    ]
    # Step 2 - Revising outline
    print("Revising outline...")
    feedback_outline = make_chat_request(client, outline_revision_msg)
    write_to_file("feedback_outline.txt", feedback_outline)
    outline_generation_msg.append(
        {
            "role": "user",
            "content": f"""
            # Draft Outline
            {init_outline}
            # Feedback
            {feedback_outline}
            """
        }
    )
    # Step 3 - Fixing Outline
    print("Fixing outline...")
    revised_outline = make_chat_request(client, outline_generation_msg)
    write_to_file("revised_outline.txt", revised_outline)
    outline_advice_msg = [
        {
            "role": "system",
            "content": _outline_advice_prompt.format(
                prev_prompt=outline_generation_prompt_pt_1,
                reply=revised_outline
            )
        }
    ]
    # Step 4 - Advising Outline
    print("Advising revised outline...")
    recent_advice = make_chat_request(client, outline_advice_msg)
    write_to_file("recent_advice.txt", recent_advice)
    # Step 5 - Generating draft for each section
    print("Generating section outline")
    section_list = extract_section_titles(recent_advice)
    print(section_list)
    final_outline = ""
    for section in section_list:
        section_outline_msg = [
            {
                "role": "system",
                "content": _section_outline_prompt.format(
                    abstracts=abstracts,
                    outline=revised_outline,
                    feedback=recent_advice,
                    section=section
                )
            }
        ]
        final_outline += make_chat_request(client, section_outline_msg)
        final_outline += "\n"
    write_to_file("outline.txt", final_outline)
    return final_outline, section_list


def enrich_section(section_list: list[str], topic: str, outline: str, abstracts: dict[int, str]):
    print("Enriching Draft...")
    directory = "enriched_sections"
    if not os.path.exists(directory):
        os.makedirs(directory)
    for section in section_list:
        summaries_combined = "\n".join([f"{key}: {value}" for key, value in abstracts.items()])
        enrich_section_msg = [
            {
                "role": "system",
                "content": _section_writer_prompt.format(
                    topic=topic,
                    outline=outline,
                    section=section,
                )
            },
            {
                "role": "user",
                "content": summaries_combined
            }
        ]
        enriched_draft = make_chat_request(client, enrich_section_msg)
        filename = f"{directory}/{get_section_filename(section)}.txt"
        write_to_file(filename, enriched_draft)
        print(f"Saved {section} to {filename}")


def get_section_filename(section):
    return section.replace(' ', '_').replace('.', '').lower()


def edit_suggestions(section_list, directory="checked_sections"):
    print("Getting Suggestions for All Sections...")

    combined_content = []

    for section in section_list:
        filename = f"{directory}/{get_section_filename(section)}.txt"
        with open(filename, 'r') as f:
            combined_content.append(f.read())

    combined_advice_msg = [
        {
            "role": "system",
            "content": _combined_section_suggestion_prompt + "\n\n".join(combined_content) + "## Suggestions\n"
        }
    ]

    # Generate a single suggestion for all sections
    combined_advice = make_chat_request(client, combined_advice_msg)
    write_to_file("combined_advice.txt", combined_advice)

    # Parse combined suggestions into a list
    parsed_suggestions = parse_suggestions(combined_advice)
    # print("parsed_suggestions", parsed_suggestions)
    # print("parsed_suggestions_length", len(parsed_suggestions))

    refined_sections = []

    # Iterate through the files two by two and apply edits
    for index in range(0, len(section_list) - 1, 2):
        refined_content = edit_two_files(
            section_list[index],
            section_list[index + 1],
            parsed_suggestions[index:index + 2]
        )
        refined_sections.append(refined_content)

    # Write all refined sections to a new file
    output_file = f"refined_all_sections.txt"
    output_content = ("\n\n".join(refined_sections)
                      .replace("Section 1: ", "")
                      .replace("Section 2: ", ""))
    write_to_file(output_file, output_content)

    print(f"All edits have been saved to {output_file}")
    return output_content


def parse_suggestions(suggestions_text):
    parsed_suggestions = []
    sections = suggestions_text.split("\n\n")

    current_block = []

    for section in sections:
        section = section.strip()
        # Check if the section starts with "Section Title"
        if section.startswith("Section Title:"):

            if current_block:
                parsed_suggestions.append("\n\n".join(current_block))
                current_block = []

            current_block.append(section)
        else:

            current_block.append(section)

    if current_block:
        parsed_suggestions.append("\n\n".join(current_block))

    return parsed_suggestions


def edit_two_files(section1, section2, suggestions):
    print(f"Editing files: {section1}, {section2}")
    directory = "enriched_sections"
    filename1 = f"{directory}/{get_section_filename(section1)}.txt"
    filename2 = f"{directory}/{get_section_filename(section2)}.txt"

    with open(filename1, 'r') as f:
        file1 = f.read()
    with open(filename2, 'r') as f:
        file2 = f.read()

    # Generate refinement suggestions for the two files
    section_refine_msg = [
        {
            "role": "system",
            "content": _section_refine_prompt.format(
                section1=file1,
                section2=file2,
            )
        },
        {
            "role": "user",
            "content": f"Suggestions for Section 1:\n{suggestions[0]}\n\n"
                       f"Suggestions for Section 2:\n{suggestions[1]}"
        }
    ]

    refinement = make_chat_request(client, section_refine_msg)
    print("Refinement for the pair:")
    print(refinement)

    return refinement


def extract_reference_numbers(sentence):
    # Match references enclosed in square brackets, with ',' or ';' as separators
    match = re.search(r'\[\d+([,;\s]*\d+)*\]', sentence)
    if match:
        # Extract the matched text, remove brackets, and split by commas or semicolons
        numbers = re.split(r'[;,\s]+', match.group(0).strip("[]"))
        return [int(num) for num in numbers if num.isdigit()]
    return []


def check_hallucination(full_context: dict[int, str], sections: list[str], source_directory="enriched_sections",
                        saved_directory="checked_sections"):
    if not os.path.exists(f"./{saved_directory}"):
        os.makedirs(f"./{saved_directory}")

    encoding = tiktoken.encoding_for_model('gpt-4o')
    for file in os.listdir(f"./{source_directory}"):
        if file.split('.')[0] in sections:
            print(f"Checking section: {file[:-4]}")
            with open(os.path.join(f"./{source_directory}", file), 'r') as f:
                sentences = f.read().split("\n")
            new_sentences = []
            for i, s in enumerate(sentences):
                ref_nums = extract_reference_numbers(s)
                tmp_s = s
                if len(ref_nums) > 0:
                    context = sentences[max(0, i - 2):min(len(sentences), i + 2)]
                    for n in ref_nums:
                        reference_paper_content = full_context[n].split("References")[0]
                        if len(encoding.encode(reference_paper_content)) > 30000:
                            continue
                        msg = [
                            {
                                "role": "system",
                                "content": _check_hallucination_prompt
                            },
                            {
                                "role": "user",
                                "content": f"""
                                        # Target Sentence
                                        {tmp_s}
                                        # Context
                                        {context}
                                        # Reference Paper Index Number - {n}
                                        {reference_paper_content}
                                        """
                            }
                        ]
                        res = make_chat_request(client, msg, model="gpt-4o", temperature=0.2, top_p=0.3)
                        time.sleep(10)
                        tmp_s = res
                new_sentences.append(tmp_s)
            print("Saving checked file...")
            new_paragraph = "\n".join(new_sentences)
            write_to_file(f"./{saved_directory}/{file}", new_paragraph)


def read_and_summarize_articles(abstracts: dict[int, str], fallback: dict[int, str] = None):
    print("Reading and Summarizing Articles...")
    # abstract_list = abstracts.strip().split("\n\n")
    summaries: dict[int, str] = {}
    encoding = tiktoken.encoding_for_model('gpt-4o')
    directory = "summarized_articles"
    if not os.path.exists(directory):
        os.makedirs(directory)
    for abstract_num in abstracts:
        try:
            # Separate abstract number and text
            # abstract_number, abstract_text = abstract.split("\n", 1)
            # abstract_number = abstract_number.strip()
            # Simulate "reading" by analyzing content and summarizing
            abstract_text = abstracts[abstract_num].split("References")[0]

            if len(encoding.encode(abstract_text)) > 30000:
                if not fallback or abstract_num not in fallback:
                    continue
                print(f"Fall back to abstract {abstract_num}")
                summary = fallback[abstract_num]
            else:
                read_and_summarize_msg = [
                    {
                        "role": "system",
                        "content": _gen_summarization_prompt
                    },
                    {
                        "role": "user",
                        "content": abstract_text
                    }
                ]
                summary = make_chat_request(client, read_and_summarize_msg, temperature=0.6, top_p=0.7)

            summaries[abstract_num] = summary
            # Save each summary to a separate file
            filename = f"{directory}/abstract_{abstract_num}.txt"
            write_to_file(filename, summary)
            print(f"Saved summary for abstract {abstract_num} to {filename}")
        except Exception as e:
            print(f"Failed to process article: {abstract_num}\nError: {e}")
    return summaries
