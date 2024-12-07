from download_abs import search_on_arxiv
from prompts import (
    _outline_generation_prompt,
    _outline_revision_prompt,
    _outline_advice_prompt,
    _section_outline_prompt,
)
from openai import OpenAI
import re


def make_chat_request(client, messages, model="gpt-4o", temperature=0.3, top_p=0.5):
    try:
        response = client.chat.completions.create(
            model=model, messages=messages, temperature=temperature, top_p=top_p
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error in OpenAI API call: {e}")


def write_to_file(filepath, content):
    try:
        with open(filepath, "w") as f:
            f.write(content)
    except IOError as e:
        raise Exception(f"Error writing to file {filepath}: {e}")


def main(topic, reference_papers):
    # reference_papers = reference_papers.split(",")
    refernece_papers_abstracts = search_on_arxiv(reference_papers)
    abstracts = ""
    for i, d in enumerate(refernece_papers_abstracts):
        abstract = d["abstract"].replace("\n", " ")
        abstracts += f"{i + 1}\n{d['title']}\n{abstract}\n\n"

    client = OpenAI()

    outline_generation_prompt_pt_1 = "\n".join(
        _outline_generation_prompt.format(topic=topic).split("\n")[2:]
    )
    # Step 1 - Generating initial outline
    print("Generating initial outline...")
    outline_generation_msg = [
        {"role": "system", "content": _outline_generation_prompt.format(topic=topic)},
        {"role": "user", "content": abstracts},
    ]
    init_outline = make_chat_request(client, outline_generation_msg)
    write_to_file("stage_1_init_outline.txt", init_outline)
    # Step 2 - Revising outline
    print("Revising outline...")
    outline_revision_msg = [
        {
            "role": "system",
            "content": _outline_revision_prompt.format(
                prev_prompt=outline_generation_prompt_pt_1, reply=init_outline
            ),
        }
    ]
    feedback_outline = make_chat_request(client, outline_revision_msg)
    write_to_file("feedback_outline.txt", feedback_outline)
    retry = 0
    while ("[x] Revision Needed" or "[x] Fail" in feedback_outline) and retry < 3:
        # Step 3 - Fixing Outline
        print("Fixing outline...")
        outline_generation_msg.append(
            {
                "role": "user",
                "content": f"""
                # Draft Outline
                {init_outline}
                # Feedback
                {feedback_outline}
                """,
            }
        )
        revised_outline = make_chat_request(client, outline_generation_msg)
        outline_generation_msg = outline_generation_msg[:-1]
        init_outline = revised_outline
        print("Revising outline...")
        outline_revision_msg = [
            {
                "role": "system",
                "content": _outline_revision_prompt.format(
                    prev_prompt=outline_generation_prompt_pt_1, reply=init_outline
                ),
            }
        ]
        feedback_outline = make_chat_request(client, outline_revision_msg)
        retry += 1
    write_to_file("feedback_outline.txt", feedback_outline)
    write_to_file("revised_outline.txt", revised_outline)
    # Step 4 - Advising Outline
    print("Advising revised outline...")
    outline_advice_msg = [
        {
            "role": "system",
            "content": _outline_advice_prompt.format(
                prev_prompt=outline_generation_prompt_pt_1, reply=revised_outline
            ),
        }
    ]
    recent_advice = make_chat_request(client, outline_advice_msg)
    write_to_file("recent_advice.txt", recent_advice)
    section_list = []
    for name in revised_outline.split("\n"):
        match = re.search(r"##\s*\d+\.\s(.*)", name)
        if match:
            section_list.append(match.group(1))
    final_outline = ""
    for section in section_list:
        section_outline_msg = [
            {
                "role": "system",
                "content": _section_outline_prompt.format(
                    abstracts=abstracts,
                    outline=revised_outline,
                    feedback=recent_advice,
                    section=section,
                ),
            }
        ]
        final_outline += make_chat_request(client, section_outline_msg)
        final_outline += "\n"
    write_to_file("final_outline.txt", final_outline)


if __name__ == "__main__":
    titles = [
        "AraLegal-BERT A pretrained language model for Arabic Legal text",
        "PromptSource An Integrated Development Environment and Repository for Natural Language Prompts",
        "Language models are few-shot learners",
        "Deep learning in law early adaptation and legal word embeddings trained on large corpora",
        "ChatGPT Goes to Law School January 23 2023",
        "Scaling instruction-finetuned language models",
        "Chatlaw Open-source legal large language model with integrated external knowledge bases",
        "A Survey on Legal Judgment Prediction Datasets Metrics Models and Challenges",
        "Bert Pre-training of deep bidirectional transformers for language understanding",
        "State of the Art in Artificial Intelligence applied to the Legal Domain",
        "Towards WinoQueer Developing a Benchmark for Anti-Queer Bias in Large Language Models",
        "Legal Textual Entailment Using Ensemble of Rule-Based and BERT-Based Method with Data Augmentation by Related Article Generation",
        "ChatGPT by OpenAI The End of Litigation Lawyers Available at SSRN httpdx",
        "Natural Language Processing in the Legal Domain",
        "ChatGPT Generative AI Systems as Quasi-Expert Legal Advice Lawyers - Case Study Considering Potential Appeal Against Conviction of Tom Hayes",
        "Crosslingual Generalization through Multitask Finetuning",
        "Law Informs Code A Legal Informatics Approach to Aligning Artificial Intelligence with Humans",
        "Leveraging Large Language Models for Topic Classification in the Domain of Public Affairs",
        "Learning Transferable Visual Models From Natural Language Supervision",
        "Exploring the limits of transfer learning with a unified text-to-text transformer",
        "Billions of parameters are worth more than in-domain training data A case study in the legal case entailment task",
        "Multitask Prompted Training Enables Zero-Shot Task Generalization",
        "Bloom A 176b-parameter openaccess multilingual language model",
        "Prompting Large Language Models with Answer Heuristics for Knowledge-based Visual Question Answering",
        "Text Classification via Large Language Models",
        "Unifying language learning paradigms",
        "Attention Is All You Need",
        "mT5 A Massively Multilingual Pretrained Text-to-Text Transformer",
        "Extractive text summarization using deep learning approach",
        "HUKB at the COLIEE 2022 statute law task",
    ]
    main("LLM applications in legal texts", titles)
