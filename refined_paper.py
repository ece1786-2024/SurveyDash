from openai import OpenAI
# import openai

from prompts import (_outline_generation_prompt,
                     _outline_revision_prompt,
                     _outline_advice_prompt,
                     _section_outline_prompt,
                     _section_writer_prompt,
                     _section_advice_prompt,
                     _section_refine_prompt,
                     _combined_section_suggestion_prompt,
                     _check_hallucination_prompt)
import tiktoken
import time
import pymupdf4llm
import urllib.request
import json
import re
import os

# client = OpenAI(api_key='')
# client = ""
# openai.api_key = "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"

def load_abstracts(filename):
    with open(f'{filename}.json', 'r') as f:
        data = json.load(f)
    text = ""
    for i, d in enumerate(data):
        abstract = d['abstract'].replace("\n", ' ')
        text += f"{i + 1}\n{d['title']}\n{abstract}\n\n"
    return text

def load_full_content(filename, pdf_directory="./reference_papers"):
    with open(f'{filename}.json', 'r') as f:
        data = json.load(f)
    full_content = {}
    need_to_download = False
    if not os.path.exists(pdf_directory):
        need_to_download = True
    for i, d in enumerate(data):
        if need_to_download:
            urllib.request.urlretrieve(d["url"].replace("abs", "pdf"), f"{pdf_directory}/{d['title']}.pdf")
        curr_content = pymupdf4llm.to_markdown(f"{pdf_directory}/{d['title']}.pdf")
        full_content[i+1] = curr_content
    return full_content

def make_chat_request(client, messages, model="gpt-4o", temperature=0.3, top_p=0.5):
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

# def make_chat_request(client, messages, model="gpt-4", temperature=0.3, top_p=0.5):

#     try:
#         response = openai.ChatCompletion.create(
#             model=model,
#             messages=messages,
#             temperature=temperature,
#             top_p=top_p
#         )
#         return response.choices[0].message['content']
#     except Exception as e:
#         raise Exception(f"Error in OpenAI API call: {e}")

def write_to_file(filepath, content):
    try:
        with open(filepath, 'w') as f:
            f.write(content)
    except IOError as e:
        raise Exception(f"Error writing to file {filepath}: {e}")
    
def extract_section_titles(recent_advice):
    pattern = r"### (\d+\.\s+[A-Za-z ]+)"
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
    return final_outline, section_list

def enrich_section(section_list, topic, outline, abstracts):
    print("Enriching Draft...")
    directory = "enriched_sections"
    if not os.path.exists(directory):
        os.makedirs(directory)
    enriched_draft = ""
    for section in section_list:
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
                "content": abstracts
            }
        ]
        enriched_draft = make_chat_request(client, enrich_section_msg)
        filename = f"{directory}/{section.replace(' ', '_').replace('.', '').lower()}.txt"
        write_to_file(filename, enriched_draft)
        print(f"Saved {section} to {filename}")
        
        
def gen_section_advice(section_list):
    print("Final Draft...")
    directory = "enriched_sections"
    refined_sections = []
    for index in range(0, len(section_list) - 1, 2): 
        filename1 = f"{directory}/{section_list[index].replace(' ', '_').replace('.', '').lower()}.txt"
        filename2 = f"{directory}/{section_list[index+1].replace(' ', '_').replace('.', '').lower()}.txt"
        with open(filename1, 'r') as f:
            file1 = f.read()
        with open(filename2, 'r') as f:
            file2 = f.read()
        section_advice_msg = [
            {
                "role": "system",
                "content": _section_advice_prompt.format(
                    section1=file1,
                    section2=file2,
                )
            }
        ]
        advice = make_chat_request(client, section_advice_msg)
        print(advice)
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
                "content": advice
            }
        ]
        refinement = make_chat_request(client, section_refine_msg)
        print(refinement)
        refined_sections.append(refinement)
    with open(f"{directory}/refined_combined_sections.txt", 'w') as f:
        for section in refined_sections:
            f.write(section + "\n\n")

def edit_suggestions(section_list):

    print("Getting Suggestions for All Sections...")
    directory = "enriched_sections"
    combined_content = []

    for section in section_list:
        filename = f"{directory}/{section.replace(' ', '_').replace('.', '').lower()}.txt"
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
    print("Generated Combined Advice:", combined_advice)

    # Parse combined suggestions into a list
    parsed_suggestions = parse_suggestions(combined_advice)
    print("parsed_suggestions", parsed_suggestions)
    print("parsed_suggestions_length", len(parsed_suggestions))

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
    output_file = f"{directory}/refined_all_sections.txt"
    with open(output_file, 'w') as f:
        for section in refined_sections:
            f.write(section + "\n\n")

    print(f"All edits have been saved to {output_file}")



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
    filename1 = f"{directory}/{section1.replace(' ', '_').replace('.', '').lower()}.txt"
    filename2 = f"{directory}/{section2.replace(' ', '_').replace('.', '').lower()}.txt"

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

def check_hallucination(full_context, section_initials, source_directory="enriched_sections", saved_directory="checked_sections"):
    if not os.path.exists(f"./{saved_directory}"):
        os.makedirs(f"./{saved_directory}")
    client = OpenAI()
    encoding = tiktoken.encoding_for_model('gpt-4o')
    for files in os.listdir(f"./{source_directory}"):
        if files[:2] in section_initials:
            print(f"Checking section: {files[:-4]}")
            with open(os.path.join(f"./{source_directory}", files), 'r') as f:
                sentences = f.read().split("\n")
            new_sentences = []
            for i, s in enumerate(sentences):
                ref_nums = extract_reference_numbers(s)
                tmp_s = s
                if len(ref_nums) > 0:
                    context = sentences[max(0, i-2):min(len(sentences), i+2)]
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
            write_to_file(f"./{saved_directory}/{files}", new_paragraph)
    return

if __name__ == "__main__":
    # topic = 'LLM applications in legal texts'
    #abstracts = load_abstracts('The_Impact_of_Large_Language_Modeling_on_Natural_Language_Processing_in_Legal_Texts_A_Comprehensive_Survey.pdf')
    # final_outline, section_list = gen_survey_outline(abstracts, topic)
    # write_to_file("outline.txt", final_outline)
    section_list = ["Introduction", "Domain-Specific LLMs for Legal Texts", "Multilingual and Cross-Lingual Capabilities", "Legal Reasoning and Societal Values in LLMs", "Future Directions and Ethical Considerations", "Conclusion"]
    full_content = load_full_content('The_Impact_of_Large_Language_Modeling_on_Natural_Language_Processing_in_Legal_Texts_A_Comprehensive_Survey.pdf')
    section_initials = ["in", "do",  "mu", "fu", "le", "co"]
    check_hallucination(full_content, section_initials)
    # with open('outline.txt', 'r') as f:
    #     final_outline = f.read()
    # enrich_section(section_list, topic, final_outline,abstracts)
    
    #method 1
    #gen_section_advice(section_list)
    
    #method 2
    # edit_suggestions(section_list)