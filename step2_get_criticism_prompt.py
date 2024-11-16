import pyperclip

from step1_get_initial_prompt import get_prompt, topic

def get_next_prompt(reply):
    prev_prompt = get_prompt(topic).split('\n')
    prev_prompt = '\n'.join(prev_prompt[2:])

    instruction = """You are a experienced professor and are extremely demanding and expects perfection from your students. You are reviewing the outline of a survey paper created by a student. Your task is to provide constructive feedback on the outline to help the student improve the structure and content of the survey paper.

You should make sure the student's outline is well-structured, coherent, and effectively conveys the main ideas and contributions of the selected papers. The student must mention all the core papers and all possible related papers in each section, but must not make up any content that is not included in the abstracts of the papers.

You must provide detailed feedback on the student's outline, highlighting areas for improvement and suggesting ways to enhance the clarity, coherence, and depth of the survey. Your feedback should be specific, actionable, and focused on guiding the student towards a more comprehensive and well-organized survey paper.

You will grade the student's outline. You are encouraged to provide detailed feedback to help the student revise and improve the outline effectively. Only give them a pass if the outline meets your high standards and expectations.
    """

    return f"""{instruction}

# Handout for Student's Outline Review

{prev_prompt}

# Student's Outline

{reply}

# Grade

- [ ] Pass
- [ ] Revision Needed
- [ ] Fail

# Feedback

"""


file = 'The_Impact_of_Large_Language_Modeling_on_Natural_Language_Processing_in_Legal_Texts_A_Comprehensive_Survey.pdf'
# file = 'The_Recent_Large_Language_Models_in_NLP.pdf'
# file = 'Multimodal_Large_Language_Models_A_Survey.pdf'

if __name__ == '__main__':
    prompt = get_next_prompt(reply="""
### Survey Paper Outline: LLM Applications in Legal Texts

#### 1. **Introduction**
   - **Main Idea**: Introduce the significance of applying Large Language Models (LLMs) to legal texts, highlighting their potential to enhance legal understanding, document analysis, and decision-making processes.
   - **Core Papers**: 1, 3, 5, 7
   - **Possible Related Papers**: 9, 13, 15
   - **Content Structure**:
     - Overview of LLMs and their relevance in the legal domain.
     - Importance of legal text analysis in jurisprudence and practical applications.
     - Summary of the advancements and challenges in this field.
     - Cohesion: Sets the stage for thematic sections on LLM applications and methodologies.

---

#### 2. **Domain-Specific Model Development**
   - **Main Idea**: Examine efforts to develop and fine-tune LLMs specifically for the legal domain.
   - **Core Papers**: 1, 3, 13
   - **Possible Related Papers**: 7, 5
   - **Content Structure**:
     - Contributions of AraLegal-BERT to Arabic legal text processing.
     - Legal judgment prediction and specialized models for this task.
     - Case study: Effectiveness of large-scale zero-shot models like monoT5 in legal entailment.
     - Comparative analysis of domain-specific versus general-purpose LLMs.
     - Gaps: Limited cross-linguistic support and resource constraints for domain-specific models.
     - Cohesion: Transition to multilingual and multitask learning approaches in legal NLP.

---

#### 3. **Multilingual and Multitask Approaches**
   - **Main Idea**: Explore how LLMs handle multilingual legal texts and multitask scenarios to enhance cross-linguistic generalization and zero-shot learning.
   - **Core Papers**: 8, 13, 15
   - **Possible Related Papers**: 3, 14
   - **Content Structure**:
     - Overview of multitask fine-tuning techniques (e.g., BLOOMZ, mT0).
     - Analysis of performance improvements in multilingual legal datasets.
     - Comparison of multilingual LLMs to language-specific models.
     - Gaps: Challenges in scaling multitask models to include legal-specific nuances.
     - Cohesion: Lead into bias and fairness in LLMs applied to legal contexts.

---

#### 4. **Bias and Fairness in Legal NLP**
   - **Main Idea**: Investigate the presence of biases in LLMs when applied to legal texts and the methods to mitigate them.
   - **Core Papers**: 6, 9
   - **Possible Related Papers**: 7, 1
   - **Content Structure**:
     - Discussion on the societal implications of biased LLMs in the legal domain.
     - Introduction of benchmarks like WinoQueer for detecting and reducing biases.
     - Examination of the role of legal standards in aligning AI behavior with societal values.
     - Gaps: Lack of comprehensive benchmarks for bias detection in legal applications.
     - Cohesion: Establish the importance of ethical AI in the deployment of LLMs for legal purposes.

---

#### 5. **Applications and Use Cases**
   - **Main Idea**: Showcase the practical applications of LLMs in legal contexts, such as document classification, case prediction, and alignment with human values.
   - **Core Papers**: 1, 3, 10
   - **Possible Related Papers**: 13, 16
   - **Content Structure**:
     - Topic classification of legal documents using LLMs in multiple languages.
     - Performance metrics and challenges in real-world deployments.
     - Success stories and limitations in legal text classification and entailment tasks.
     - Cohesion: Relate the applications back to ethical and technical considerations.

---

#### 6. **Challenges and Future Directions**
   - **Main Idea**: Identify challenges in applying LLMs to legal texts and propose future research directions.
   - **Core Papers**: 3, 7, 5
   - **Possible Related Papers**: 15, 9
   - **Content Structure**:
     - Discussion on the gap between machine and human performance.
     - Open problems in dataset availability, multilingual support, and explainability.
     - Future opportunities in cross-domain learning and better societal alignment.
     - Cohesion: Conclude by tying these challenges to the introductory vision for LLMs in legal domains.

---

#### 7. **Conclusion**
   - **Main Idea**: Summarize the insights gained from the survey and reinforce the importance of advancing LLM applications in the legal domain.
   - **Core Papers**: All relevant papers referenced across sections.
   - **Possible Related Papers**: N/A
   - **Content Structure**:
     - Recap of key advancements in LLMs for legal text analysis.
     - Emphasis on interdisciplinary collaboration between NLP researchers and legal experts.
     - Closing thoughts on the ethical, technical, and practical impacts of this research field. 

This structured outline organizes the survey around core themes, providing a cohesive narrative that captures both the current state and future potential of LLMs in legal texts.
    """)
    pyperclip.copy(prompt)
