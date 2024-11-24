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

output = """
## Outline for "LLM Applications in Legal Texts"

### 1. Introduction
  - **Main Idea:** Introduce the importance and growing impact of Large Language Models (LLMs) in the legal domain, highlighting the challenges and opportunities in processing legal texts.
  - **Core Papers:** 1, 3, 5, 7
  - **Possible Related Papers:** 9, 10
  - **Content Structure:** 
    - Overview of the legal domain's complexity and its unique linguistic characteristics.
    - Discuss the motivation behind applying LLMs to legal texts, inspired by their success in other domains.
    - Briefly mention the gap in existing studies that this survey aims to address, particularly focusing on LLMs' adaptation to and performance in legal tasks.
  - **Cohesion Across Sections:** This section sets the stage for discussing various models, tasks, and advancements in subsequent sections.

### 2. Pre-trained Language Models for Legal Texts
  - **Main Idea:** Exploration of existing pre-trained models specifically tailored to the legal domain, and their adaptation for such tasks.
  - **Core Papers:** 1, 3, 5
  - **Possible Related Papers:** 13, 16
  - **Content Structure:** 
    - Discuss the development and implications of models like AraLegal-BERT (1) and others tailored for legal text processing.
    - Comparison of these models with general LLMs to comment on their effectiveness and necessity in the legal field.
    - Highlight the performance metrics and specific legal tasks where these models excel or fall short.
  - **Cohesion Across Sections:** Transition into the next section by outlining the challenges these models face, leading into a discussion of innovative adaptations and generalizations.

### 3. Innovative Approaches and Techniques
  - **Main Idea:** Investigation into recent innovative techniques like multitask learning, transfer learning, and bias mitigation in legal text processing.
  - **Core Papers:** 3, 6, 8
  - **Possible Related Papers:** 14, 15, 18
  - **Content Structure:** 
    - Describe multitask learning and transfer learning techniques (3, 8) that enhance model generalization across legal tasks.
    - Address the mitigation of biases and ethical considerations through techniques and benchmarks like WinoQueer (6).
    - Highlight how these approaches offer promising directions to overcome existing limitations.
  - **Cohesion Across Sections:** Connect with previous and next sections by exploring how these innovations may fit into existing legal-specific models and their applications.

### 4. Applications and Real-world Use Cases
  - **Main Idea:** Delve into the practical applications and success stories of LLMs in the legal domain, including predictive tasks and information retrieval.
  - **Core Papers:** 3, 10, 13
  - **Possible Related Papers:** 5, 16
  - **Content Structure:** 
    - Discuss specific applications such as Legal Judgment Prediction (3), topic classification in public affairs (10), and case entailment (13).
    - Evaluate how LLMs enhance efficiency and accuracy in legal document processing and decision-making.
    - Discuss potential areas of improvement and the role of human oversight.
  - **Cohesion Across Sections:** Lead into the conclusion by reflecting on applications' impact on the legal industry and the implications for future research.

### 5. Challenges, Limitations, and Future Directions
  - **Main Idea:** Critically address the challenges and limitations faced by LLMs in legal text processing and propose future directions.
  - **Core Papers:** 7, 9, 13
  - **Possible Related Papers:** 16, 17
  - **Content Structure:** 
    - Highlight the limitations regarding data availability, model interpretability, and ethical considerations.
    - Discuss societal and legal implications such as "Law Informs Code" (9).
    - Propose future research directions focusing on increasing model accountability, data diversity, and interpretability.
  - **Cohesion Across Sections:** Concludes prior discussions by summarizing the lessons learned and suggesting a pathway forward in both academia and industry.

### 6. Conclusion
  - **Main Idea:** Summarize the insights gathered from the survey and emphasize the transformative potential of LLMs in the legal domain.
  - **Core Papers:** 1, 3, 5
  - **Possible Related Papers:** 9, 10
  - **Content Structure:** 
    - Recap the main findings regarding the state-of-the-art in legal NLP, highlighting key advancements and persistent challenges.
    - Assert the importance of interdisciplinary collaboration between legal and AI researchers for advancing the field.
    - Final thoughts on the evolving landscape of legal NLP and the critical role LLMs play in shaping its future.
  - **Cohesion Across Sections:** Reinforce overarching themes of the paper, tying back to issues raised in the introduction and expanded throughout the review.
"""
