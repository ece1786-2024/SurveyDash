from openai import OpenAI
from prompts import (_outline_generation_prompt,
                     _outline_revision_prompt,
                     _outline_advice_prompt,
                     _section_outline_prompt,
                     _section_writer_prompt,
                     _section_advice_prompt,
                     _section_refine_prompt)
import json
import re
import os

client = OpenAI(api_key='')


def load_abstracts(filename):
    with open(f'{filename}.json', 'r') as f:
        data = json.load(f)
    text = ""
    for i, d in enumerate(data):
        abstract = d['abstract'].replace("\n", ' ')
        text += f"{i + 1}\n{d['title']}\n{abstract}\n\n"
    return text

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
                reply=""
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

if __name__ == "__main__":
    topic = 'LLM applications in legal texts'
    abstracts = load_abstracts('The_Impact_of_Large_Language_Modeling_on_Natural_Language_Processing_in_Legal_Texts_A_Comprehensive_Survey.pdf')
    # final_outline, section_list = gen_survey_outline(abstracts, topic)
    # write_to_file("outline.txt", final_outline)
    section_list = ["Introduction", "Domain-Specific LLMs for Legal Texts", "Multilingual and Cross-Lingual Capabilities", "Legal Reasoning and Societal Values in LLMs", "Future Directions and Ethical Considerations", "Conclusion"]
    # with open('outline.txt', 'r') as f:
    #     final_outline = f.read()
    # enrich_section(section_list, topic, final_outline,abstracts)
    gen_section_advice(section_list)