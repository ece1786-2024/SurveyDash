import pyperclip

from step1_get_initial_prompt import get_prompt, topic
from step1_get_initial_prompt import output as output1


def get_feedback_prompt(reply):
    prev_prompt = get_prompt(topic).split('\n')
    prev_prompt = '\n'.join(prev_prompt[2:])

    instruction = """You are a experienced professor and are extremely demanding and expects perfection from your students. You are reviewing the outline of a survey paper created by a student. Your task is to provide constructive feedback on the outline to help the student improve the structure and content of the survey paper.

You should make sure the student's outline is well-structured, coherent, and effectively conveys the main ideas and contributions of the selected papers. The student must mention all the related papers in each section, but must not make up any content that is not included in the abstracts of the papers.

You must provide detailed feedback on the student's outline, highlighting areas for improvement and suggesting ways to enhance the clarity, coherence, and depth of the survey. Think critically about the arrangement of sections and the connections between papers. Your feedback should be specific, actionable, and focused on guiding the student towards a more comprehensive and well-organized survey paper.

You will grade the student's outline. Only give them a pass if the outline meets your high standards and expectations. You are encouraged to provide detailed feedback to help the student revise and improve the outline effectively. You must comment on the structure of the outline, ensuring that the student is on the right track to create a successful survey paper. Give general advice on how to improve the outline and then provide specific feedback on each section.
"""

    return f"""{instruction}

# Handout for Student's Outline Review

{prev_prompt}

# Student's Outline

{reply}

# Grade

- [ ] Accept
- [ ] Minor Revision
- [ ] Major Revision
- [ ] Reject

# Feedback

"""


file = 'The_Impact_of_Large_Language_Modeling_on_Natural_Language_Processing_in_Legal_Texts_A_Comprehensive_Survey.pdf'
# file = 'The_Recent_Large_Language_Models_in_NLP.pdf'
# file = 'Multimodal_Large_Language_Models_A_Survey.pdf'

if __name__ == '__main__':
    prompt = get_feedback_prompt(reply=output1)
    pyperclip.copy(prompt)

output = """
## General Feedback

The outline presented covers key areas relevant to the application of Large Language Models (LLMs) in legal texts, but there are significant areas needing improvement to meet the high standards expected. While the student demonstrates an understanding of grouping related papers and setting thematic sections, the cohesion and depth of analysis require enhancement. A more robust linkage of themes across sections and a thorough evaluation of each paper’s contributions and their interrelations are essential. More specificity in the content descriptions and clarity in how the papers support your discussions will strengthen the coherence and quality of the paper.

### Specific Feedback on Each Section

### 1. Introduction
- **Comments:** The selection of core and possible related papers seems appropriate for providing a background on LLM usage in legal texts. However, further specificity regarding the challenges and gaps in existing research as documented in the papers should be mentioned.
- **Suggestions:** Provide clear definitions of terminologies such as LLMs within the legal context using insights from the related papers. Furthermore, clarify what unique perspectives this survey hopes to contribute to the field as identified in the abstracts.

### 2. Pre-trained Language Models for Legal Texts
- **Comments:** The section aims to discuss pre-trained models like AraLegal-BERT. However, the abstraction level needs refinement.
- **Suggestions:** More detailed comparison and contrast of the capabilities and limitations from each core paper must be included. Specify the nature of the datasets and tasks these models were tested on (information available in abstracts) and assess their competitive performance in legal tasks across different regions or languages to provide deeper insight.

### 3. Innovative Approaches and Techniques
- **Comments:** This section touches on promising technical directions but lacks depth regarding how these approaches alter or improve existing legal text processing methodologies.
- **Suggestions:** Delve more deeply into how multitask learning and bias mitigation (papers 6, 3, 8) directly improve current models over existing baselines. Illustrate these findings using results and reasoning outlined in the abstracts that might point to particular strengths or weaknesses.

### 4. Applications and Real-world Use Cases
- **Comments:** While examples of LLM applications in the legal domain are outlined, this section requires greater elaboration on how LLMs practically transform workflows.
- **Suggestions:** Include more precise case studies from the abstracts to showcase LLM application results and their implications on legal outcomes and processes. Construct a narrative that emphasizes the advantages of using LLMs over traditional methods in the real-world context, as highlighted in these papers.

### 5. Challenges, Limitations, and Future Directions
- **Comments:** This section appropriately addresses challenges but can expand to offer more concrete evidence-based conclusions on weaknesses or gaps in the literature and technological constraints.
- **Suggestions:** Discuss specific instances where current models fall short in real-world legal applications (referring to data in abstracts). Use examples from the papers to consider how these challenges might be approached to complement or extend the existing literature.

### 6. Conclusion
- **Comments:** The conclusion points are aligned with the primary focus of the survey but need to reinforce key findings effectively.
- **Suggestions:** Synthesize insights from individual sections to provide a cohesive final message. Stresses should be put on the justified merits of interdisciplinary collaboration and address opportunities for technological enhancements, backed with insights from core papers.

### Grade

- [ ] Accept
- [ ] Minor Revision
- [x] Major Revision
- [ ] Reject

### Additional Suggestions

- Ensure that each section doesn’t merely summarize findings but evaluates the contributions of each paper critically.
- Clarify the criteria used to classify core and possible related papers in each section.
- Enhance transitions between sections to develop a continuous and engaging narrative for the reader.
- Integrate some diagrams or tables in the full draft for better illustration and comparison where applicable.

With these improvements, the outline can achieve a level of thoroughness and clarity that matches high academic standards expected in survey papers.
"""
