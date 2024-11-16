import json
import pyperclip


def get_prompt(topic):
    with open(f'{file}.json', 'r') as f:
        data = json.load(f)

    text = f"""You are a experienced professor preparing a survey paper. Your task is to create a structured outline for the survey based on the papers you’ve read. This outline should help organize your analysis and highlight key themes.

## Outline the Structure

Divide your outline into thematic sections from introduction to conclusion. Each section should cover a main idea, group related papers, and outline how these studies contribute to your understanding of the topic.

## General Requirements

Think step by step. Compare and combine the abstracts across different papers prior to creating the outline. You must draft the outline of the survey paper only based on the given papers. Using content that are not included in the abstracts is strictly prohibited. 

## Outline Template

For each section, use the following template to include the following details:

1. [Title: Create a concise title that reflects the section’s primary focus or theme.]
  - [Main Idea: Summarize the core concept or question that this section will address.]
  - [Core Papers: List the IDs of the papers relevant to this section. Write only indexes in the format: 1, 2, 3.]
  - [Possible Related Papers: List the IDs of the papers that could be relevant to this section. Write only indexes in the format: 1, 2, 3.]
  - [Content Structure: Briefly outline the content of the section, including: A summary of each paper’s contributions. Comparisons or contrasts among the papers. Any gaps or unresolved issues identified in this group of papers.]
  - [Cohesion Across Sections: Consider adding notes on how sections connect to build a cohesive narrative for the review.]


# This time, you are focusing on the topic: {topic}.

## Papers

"""

    for i, d in enumerate(data):
        abstract = d['abstract'].replace("\n", ' ')
        text += f"{i + 1}\n{d['title']}\n{abstract}\n\n"

    return text


file = 'The_Impact_of_Large_Language_Modeling_on_Natural_Language_Processing_in_Legal_Texts_A_Comprehensive_Survey.pdf'
# file = 'The_Recent_Large_Language_Models_in_NLP.pdf'
# file = 'Multimodal_Large_Language_Models_A_Survey.pdf'

topic = 'LLM applications in legal texts'

if __name__ == '__main__':
    pyperclip.copy(get_prompt(topic))
