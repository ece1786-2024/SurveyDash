from openai import OpenAI
from prompts import (_outline_generation_prompt,
                     _outline_revision_prompt,
                     _outline_advice_prompt,
                     _section_outline_prompt)
import json
import re

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

def gen_survey_outline(filename, topic):
    client = OpenAI()

    abstracts = load_abstracts(filename)
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
    # TODO: This is a hard-code section title detection!!! NEED TO BE CHANGED
    section_list = [name[8:] for name in recent_advice.split("\n") if re.match("\d+\.\s", name)]
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
    return final_outline

if __name__ == "__main__":
    final_outline = gen_survey_outline(
        'The_Impact_of_Large_Language_Modeling_on_Natural_Language_Processing_in_Legal_Texts_A_Comprehensive_Survey.pdf',
        'LLM applications in legal texts'
    )
    write_to_file("outline.txt", final_outline)