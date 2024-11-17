import pyperclip

from step1_get_initial_prompt import get_prompt, topic
from step1_get_initial_prompt import output as output1
from step2_get_criticism_prompt import output as output2


def get_revision_prompt(reply, comment):
    prev_prompt = get_prompt(topic).split('\n')
    curr_prompt = """
You have written the outline of the survey paper based on the papers you’ve read. You asked your colleague to review the outline and provide feedback. Now, you must revise the outline based on the feedback received. You can consider restructuring the outline, adding more details, or improving the coherence between sections. When you realizes mistakes or flaws, acknowledge the realization. Your goal is to enhance the outline to meet the high standards expected by your colleague. Make sure to address the feedback provided and improve the outline accordingly.
"""

    prev_prompt = prev_prompt[:1] + [curr_prompt] + prev_prompt[1:]
    prev_prompt = '\n'.join(prev_prompt)

    return f"""{prev_prompt}

# Draft Outline

{reply}

# Feedback

{comment}
"""


file = 'The_Impact_of_Large_Language_Modeling_on_Natural_Language_Processing_in_Legal_Texts_A_Comprehensive_Survey.pdf'
# file = 'The_Recent_Large_Language_Models_in_NLP.pdf'
# file = 'Multimodal_Large_Language_Models_A_Survey.pdf'

if __name__ == '__main__':
    prompt = get_revision_prompt(reply=output1, comment=output2)
    pyperclip.copy(prompt)

output = """
# Revised Outline for "LLM Applications in Legal Texts"

## 1. Introduction
- **Main Idea:** Establish the foundational context for the application of Large Language Models (LLMs) in the legal domain, focusing on the challenges and opportunities these models present.
- **Core Papers:** 1, 3, 5, 7
- **Possible Related Papers:** 9, 10
- **Content Structure:** 
  - Introduction to LLMs and their significance in interpreting complex legal texts.
  - Definition of key terminologies such as "LLMs" and brief introduction to their common uses in the legal domain (inspiration from paper 1 and 7).
  - Exploration of the current gap in literature regarding LLM adaptation in legal contexts and the objectives of this survey.
  - Mention specific research insights from the core papers addressing these gaps.
  - **Cohesion Across Sections:** Sets the stage by outlining key themes that will be expanded in subsequent sections, particularly focused on models, methodologies, and challenges.

## 2. Pre-trained Language Models for Legal Texts
- **Main Idea:** Discuss current pre-trained language models developed for legal text processing and compare their effectiveness.
- **Core Papers:** 1, 3, 5
- **Possible Related Papers:** 13, 16
- **Content Structure:** 
  - Detailed comparison of AraLegal-BERT and similar models (1, 3) with traditional models like BERT (4).
  - Analysis of datasets (from paper 1 and 3) utilized in testing these models for different legal tasks.
  - Discussion of the performance in various linguistic and regional contexts and the specific legal tasks they excel in.
  - **Cohesion Across Sections:** Lead into challenges faced by introducing specific shortcomings or areas lacking robust performance metrics, segueing into innovative techniques.

## 3. Innovative Approaches and Techniques
- **Main Idea:** Examine innovative techniques such as multitask learning, transfer learning, and bias mitigation to improve legal text processing.
- **Core Papers:** 3, 6, 8
- **Possible Related Papers:** 14, 15, 18
- **Content Structure:** 
  - Explore how multitask learning (3, 8) has been used to enhance adaptability and performance in legal contexts.
  - Assess bias-mitigation strategies like those seen in WinoQueer (6) and their impact on results.
  - Evaluate how these approaches offer solutions to limitations identified in earlier sections.
  - **Cohesion Across Sections:** Link these innovations to real-world applications in the following section, indicating their practical benefits and ongoing research initiatives.

## 4. Applications and Real-world Use Cases
- **Main Idea:** Highlight successful applications of LLMs within the legal domain and illustrate the impact on legal workflows.
- **Core Papers:** 3, 10, 13
- **Possible Related Papers:** 5, 16
- **Content Structure:** 
  - Present detailed case studies such as Legal Judgment Prediction (3) or Topic Classification in Public Affairs (10) using LLMs.
  - Highlight comparative advantages over traditional legal methods and the transformative effect on legal processes.
  - Discuss the scope for improvement and the essential collaboration between AI and legal practitioners for optimal integration.
  - **Cohesion Across Sections:** Provide a segue to challenges and limitations, pointing out where these applications may not yet meet expectations.

## 5. Challenges, Limitations, and Future Directions
- **Main Idea:** Identify technical and ethical challenges and propose future research directions for LLM applications in legal texts.
- **Core Papers:** 7, 9, 13
- **Possible Related Papers:** 16, 17
- **Content Structure:**
  - Discuss limitations in data availability, model interpretability, and ethical issues using insights from papers 7 and 9.
  - Consider societal implications and the interplay between law and code as a guidance mechanism (9).
  - Propose strategies for future research focused on enhancing data diversity, accountability, and interpretability of LLMs.
  - **Cohesion Across Sections:** This section synthesizes the survey's findings and points towards actionable insights, correlating with future directions in concluding thoughts.

## 6. Conclusion
- **Main Idea:** Summarize the main findings of the survey, reiterating the role of LLMs in transforming legal text analysis, while emphasizing the need for continued interdisciplinary collaboration.
- **Core Papers:** 1, 3, 5
- **Possible Related Papers:** 9, 10
- **Content Structure:** 
  - Consolidate insights regarding state-of-the-art LLM applications in the legal field.
  - Summarize key advancements, pressing challenges, and the need for interdisciplinary research partnerships.
  - Reflect on the evolving landscape of LLMs in legal contexts and pinpoint areas ripe for continued exploration and development.
  - **Cohesion Across Sections:** Reinforce themes and insights discussed throughout the paper, ensuring a resonant conclusion that echoes the introduction.

### Additional Enhancements:
- Criteria for selecting core and related papers are now clarified within each section, based on thematic relevance and depth of analysis within the abstracts.
- Enhanced narrative transitions now provide smoother progression between sections, underscoring the continual thread of survey content.
- Incorporation of remaining feedback ensures robust structures that critically evaluate and contextualize all reviewed papers.
"""
