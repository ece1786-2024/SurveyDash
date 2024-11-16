import pyperclip

from step1_get_initial_prompt import get_prompt, topic

def get_revision_prompt(reply, comment):
    prev_prompt = get_prompt(topic)
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
    prompt = get_revision_prompt(reply="""
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
    """, comment="""
# Comprehensive Review of Survey Paper Outline: LLM Applications in Legal Texts

## Overall Assessment: Revision Needed

### Structural Strengths
1. Clear thematic organization with logical progression
2. Consistent section formatting
3. Good attention to cohesion between sections

### Major Issues Requiring Revision

#### 1. Introduction Section
- **Critical Gap**: Missing foundational papers (4, 17) that establish the basis of transformer architecture and BERT
- **Improvement Needed**: Include technical foundation before jumping to legal applications
- **Action Item**: Restructure to include:
  - Brief history of transformer-based models
  - Transition to legal domain applications
  - Current challenges and opportunities

#### 2. Domain-Specific Model Development
- **Misalignment**: Over-emphasis on AraLegal-BERT while missing broader context
- **Missing Connection**: No clear link to Paper 4 (original BERT) for comparative analysis
- **Action Item**: Expand section to include:
  - Comparison with base BERT architecture
  - Systematic analysis of domain adaptation techniques
  - Clear metrics for performance evaluation

#### 3. Multilingual and Multitask Approaches
- **Technical Oversight**: Missing critical discussion from Paper 18 (mT5)
- **Integration Gap**: Need stronger connection to Papers 2 and 12
- **Action Item**: Include:
  - Detailed analysis of prompt-based approaches
  - Cross-lingual transfer mechanisms
  - Comparative analysis of different multilingual models

#### 4. Bias and Fairness Section
- **Scope Issue**: Over-reliance on WinoQueer (Paper 6) which isn't specifically legal-focused
- **Missing Context**: Insufficient integration with Paper 9's legal informatics approach
- **Action Item**: Refocus section on:
  - Legal-specific bias concerns
  - Regulatory compliance
  - Ethical frameworks in legal AI

#### 5. Applications Section
- **Coverage Gap**: Insufficient discussion of transfer learning (Paper 12)
- **Integration Need**: Missing connection to Paper 16's classification framework
- **Action Item**: Expand to include:
  - Systematic comparison of different application approaches
  - Real-world deployment considerations
  - Performance metrics across different legal tasks

### Technical Accuracy Concerns
1. Several papers are cited out of context
2. Missing technical details from key methodological papers
3. Insufficient discussion of evaluation metrics from Paper 3

### Recommendations for Improvement

1. **Technical Foundation**
   - Add section on fundamental LLM architectures
   - Include clear progression from general to legal-specific models

2. **Methodology Coverage**
   - Expand discussion of training approaches
   - Include detailed analysis of evaluation metrics
   - Add cross-model comparisons

3. **Literature Integration**
   - Better incorporate Papers 11, 12, and 14 for technical depth
   - Strengthen connections between sections
   - Add comparative analysis across different approaches

4. **Applications Framework**
   - Develop clearer categorization of applications
   - Include performance metrics
   - Add implementation considerations

### Required Reading
Before revision, carefully review:
1. Paper 4 (BERT) - fundamental architecture
2. Paper 17 (Attention) - technical foundation
3. Paper 12 (T5) - transfer learning framework
4. Paper 18 (mT5) - multilingual approaches

## Grade: Revision Needed

The outline shows promise but requires substantial revision to meet the standards expected of a comprehensive survey paper. Focus particularly on technical accuracy, proper paper integration, and methodological clarity.

### Next Steps
1. Revise structure incorporating feedback
2. Strengthen technical foundations
3. Better integrate all provided papers
4. Resubmit with detailed attention to evaluation metrics and comparative analysis
    """)
    pyperclip.copy(prompt)
