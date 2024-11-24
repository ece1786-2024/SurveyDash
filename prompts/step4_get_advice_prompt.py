import pyperclip

from step1_get_initial_prompt import get_prompt, topic
from step3_get_revision_prompt import output as output3


def get_feedback_prompt(reply):
    prev_prompt = get_prompt(topic).split('\n')
    prev_prompt = '\n'.join(prev_prompt[2:])

    instruction = """You are a experienced professor and are extremely demanding and expects perfection from your students. You are reviewing the outline of a survey paper created by a student. Your task is to provide constructive feedback on the outline to help the student improve the structure and content of the survey paper.

You should make sure the student's outline is well-structured, coherent, and effectively conveys the main ideas and contributions of the selected papers. The student must mention all the core papers and all possible related papers in each section, but must not make up any content that is not included in the abstracts of the papers.

The student hand back the revised outline to you and will proceed to write each section of the survey paper based on your next feedback. You must highlight areas for improvement and suggesting ways to enhance the clarity, coherence, and depth of the survey. Your feedback should be specific, actionable, and focused on guiding the student towards a more comprehensive and well-organized survey paper. Your feedback should be detailed and provide clear directions for the student to follow on writing each section.
"""

    return f"""{instruction}

# Handout for Student's Outline Review

{prev_prompt}

# Student's Outline

{reply}

# Feedback on revision

# Suggestions for writing each section
 
## General Requirements

"""


file = 'The_Impact_of_Large_Language_Modeling_on_Natural_Language_Processing_in_Legal_Texts_A_Comprehensive_Survey.pdf'
# file = 'The_Recent_Large_Language_Models_in_NLP.pdf'
# file = 'Multimodal_Large_Language_Models_A_Survey.pdf'

if __name__ == '__main__':
    prompt = get_feedback_prompt(reply=output3)
    pyperclip.copy(prompt)

output = """
## Feedback on Revised Outline

Thank you for providing a comprehensive revised outline for your survey paper on "LLM Applications in Legal Texts." You've made solid progress in structuring the paper, but there are key areas that need improvement to ensure a coherent, in-depth survey that accurately reflects the contributions of the selected papers. Below are detailed suggestions for each section.

### 1. Introduction

**Improvements Needed:**
- Ensure the **core concepts** are clearly articulated; specifically, what role LLM applications in legal texts have played so far and the potential they hold.
- The **gap in literature** should be clearly identified with explicit references from the abstracts that indicate this. Use paper 7 more effectively to demonstrate trends in NLP & Legal applications.
- **Cohesion**: Be explicit about how this section establishes themes that will be explored in detail in subsequent sections.

**Suggestions:**
- Use direct findings from paper 1 and 3 to introduce specific challenges and opportunities these models present.
- Clearly define what you mean by LLMs' adaptation to legal contexts – is it processing efficiency, understanding nuances, or integration into workflows?

### 2. Pre-trained Language Models for Legal Texts

**Improvements Needed:**
- The **effectiveness comparisons** should be more explicit. Establish clear criteria for evaluating effectiveness based on the abstracts (e.g., accuracy, adaptability, linguistic coverage).
- Discuss the **coverage of languages and legal systems** examined in these papers.

**Suggestions:**
- Expand on how paper 1’s AraLegal-BERT was optimized, and how it compares to paper 4’s BERT.
- Elaborate on the datasets used and their relevancy as stressed in paper 3 and 5.
 
### 3. Innovative Approaches and Techniques

**Improvements Needed:**
- Deepen the **analysis** of how innovative techniques are applied and their impact on the effectiveness of legal text processing.
- Explain why techniques such as multitask learning and bias mitigation are **imperative** as drawn from the depths of the related abstracts.

**Suggestions:**
- Emphasize on paper 8's introduction to Multitask Finetuning and how it could beneficially crossover into legal text applications.
- Explore bias mitigation in legal texts using parallels from paper 6's findings.

### 4. Applications and Real-world Use Cases

**Improvements Needed:**
- **Illustrate the use cases** with more precision. Identify metrics or outcomes from the papers that can help establish these applications' value.
- Examine paper 10 carefully to ensure coverage of its insights on LLMs' effectiveness in public affairs which you need to extrapolate on legal contexts.

**Suggestions:**
- Utilize paper 3 (Legal Judgment Prediction) extensively, as it is a directly relevant application within the legal domain.
- More directly highlight transformative impacts referenced in paper 13.

### 5. Challenges, Limitations, and Future Directions

**Improvements Needed:**
- Develop a more detailed and critical **evaluation** of challenges.
- Ethical considerations (from paper 9) should be expanded to reflect more comprehensive societal implications.

**Suggestions:**
- Use paper 7 to draw attention to specific technical gaps in NLP & Law that need to be addressed.
- Bring paper 9's perspective into a sharper focus when discussing the alignment of AI and human legal needs.

### 6. Conclusion

**Improvements Needed:**
- Ensure a **well-rounded summary** that does not just echo previous sections but instead integrates the survey's key insights with future perspectives.
- Strong closing remarks indicating **future trends or emerging research** directions.

**Suggestions:**
- Use the potential interdisciplinary impact highlighted in papers 1 and 5 to close the loop on how these advances might shape the next decade of legal research and practice.

### Additional Considerations:

- Your **section transitions** indeed need smoothing; consider using phrases that bridge topics, showing how each section feeds into the subsequent one.
- Where you see **gaps or emerging questions**, make clear references to them and relate these to ongoing research needs or potential future studies.

With these improvements, your survey paper will better reflect the detail and depth needed to critically assess and convey the state-of-the-art and potential of LLM applications in legal texts. Focus on deepening the analysis and ensuring smooth, logical flow throughout the sections.

"""
