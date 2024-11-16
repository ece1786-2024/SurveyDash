import pyperclip

from step1_get_initial_prompt import get_prompt, topic

def get_next_prompt(reply):
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
    prompt = get_next_prompt(reply="""
Let me revise the outline incorporating the feedback. I'll structure it to better reflect the technical foundations and ensure proper integration of all papers.

# Revised Survey Paper Outline: LLM Applications in Legal Texts

#### 1. **Introduction and Technical Foundations**
   - **Main Idea**: Establish the technical foundations of transformer-based models and their evolution toward legal applications
   - **Core Papers**: 4, 17, 12
   - **Possible Related Papers**: 5, 7
   - **Content Structure**:
     - Development of transformer architecture and attention mechanisms
     - Evolution from BERT to specialized legal models
     - Current challenges and opportunities in legal domain adaptation
     - Technical requirements for legal text processing
   - **Cohesion**: Links technical foundations to domain-specific applications

---

#### 2. **Transfer Learning and Model Architecture**
   - **Main Idea**: Analyze the progression from general-purpose LLMs to legal domain adaptation
   - **Core Papers**: 4, 12, 18
   - **Possible Related Papers**: 1, 13
   - **Content Structure**:
     - BERT architecture and its impact on legal NLP
     - T5's unified text-to-text framework
     - Comparison of transfer learning approaches
     - Analysis of model scaling effects on legal tasks
   - **Cohesion**: Bridges general architectures to legal specialization

---

#### 3. **Domain-Specific Models and Adaptation**
   - **Main Idea**: Examine specialized legal models and adaptation techniques
   - **Core Papers**: 1, 13, 3
   - **Possible Related Papers**: 4, 12
   - **Content Structure**:
     - Comparative analysis with base BERT architecture
     - Domain adaptation techniques and their effectiveness
     - Case study: AraLegal-BERT vs. general BERT
     - Evaluation metrics and performance benchmarks
   - **Cohesion**: Links to multilingual approaches

---

#### 4. **Multilingual and Cross-lingual Approaches**
   - **Main Idea**: Analyze multilingual capabilities in legal text processing
   - **Core Papers**: 18, 8, 15
   - **Possible Related Papers**: 2, 14
   - **Content Structure**:
     - mT5's multilingual architecture and capabilities
     - Cross-lingual transfer in legal applications
     - Prompt-based approaches for multilingual tasks
     - Evaluation across different legal systems
   - **Cohesion**: Connects to practical applications

---

#### 5. **Prompting and Task Adaptation**
   - **Main Idea**: Examine prompt engineering and task adaptation in legal contexts
   - **Core Papers**: 2, 14, 16
   - **Possible Related Papers**: 8, 12
   - **Content Structure**:
     - PromptSource methodology and applications
     - Zero-shot and few-shot learning in legal tasks
     - Task-specific prompting strategies
     - Performance analysis across different legal tasks
   - **Cohesion**: Links to practical applications

---

#### 6. **Applications and Implementation**
   - **Main Idea**: Analyze practical applications and deployment considerations
   - **Core Papers**: 10, 13, 16
   - **Possible Related Papers**: 3, 7
   - **Content Structure**:
     - Legal document classification systems
     - Case prediction and analysis
     - Implementation challenges and solutions
     - Performance metrics and benchmarks
   - **Cohesion**: Connects to ethical considerations

---

#### 7. **Legal Alignment and Ethical Considerations**
   - **Main Idea**: Address alignment with legal standards and ethical implications
   - **Core Papers**: 9, 7
   - **Possible Related Papers**: 6, 15
   - **Content Structure**:
     - Legal standards for AI systems
     - Bias detection and mitigation
     - Regulatory compliance frameworks
     - Ethical considerations in legal AI
   - **Cohesion**: Links to future directions

---

#### 8. **Future Directions and Challenges**
   - **Main Idea**: Identify open problems and research opportunities
   - **Core Papers**: 3, 7, 15
   - **Possible Related Papers**: 9, 13
   - **Content Structure**:
     - Technical challenges in model development
     - Data availability and quality issues
     - Cross-jurisdictional adaptation needs
     - Integration with legal practice
   - **Cohesion**: Connects back to introduction

This revised outline:
1. Establishes stronger technical foundations
2. Better integrates all provided papers
3. Provides clearer progression from general to specific topics
4. Includes more detailed technical analysis
5. Addresses evaluation metrics throughout sections

The structure now better reflects the technical depth required while maintaining focus on legal applications.
    """)
    pyperclip.copy(prompt)

"""

# Comprehensive Feedback on Legal LLM Survey Paper Outline

## Overall Structure Assessment
The outline demonstrates good organization but requires some adjustments to achieve the necessary academic rigor and comprehensive coverage. Here's my detailed feedback and writing guidelines for each section:

## Section-by-Section Writing Guidelines

### 1. Introduction and Technical Foundations

#### Strengths:
- Good connection between technical foundations and domain application
- Appropriate core paper selection (4, 17, 12)

#### Areas for Improvement:
- Need stronger motivation for legal domain application
- Technical progression needs more structure

#### Writing Guidelines:
1. Begin with a clear problem statement from Paper 7, emphasizing the growing importance of NLP in legal domain
2. Present chronological development:
   - Start with Transformer architecture (Paper 17)
   - Transition to BERT (Paper 4)
   - Progress to T5 framework (Paper 12)
3. Each model discussion should include:
   - Key architectural innovations
   - Breakthrough capabilities
   - Relevance to legal applications
4. End with specific challenges in legal domain adaptation

### 2. Transfer Learning and Model Architecture

#### Strengths:
- Good technical foundation papers
- Clear progression logic

#### Areas for Improvement:
- Need more explicit connection to legal domain
- Should include scaling analysis from Paper 13

#### Writing Guidelines:
1. Begin with BERT's transfer learning framework (Paper 4):
   - Pre-training objectives
   - Fine-tuning methodology
2. Analyze T5's contributions (Paper 12):
   - Text-to-text framework benefits
   - Performance comparisons
3. Include mT5 architecture (Paper 18) focusing on:
   - Multilingual capabilities
   - Adaptation to legal domain
4. Incorporate Paper 13's findings on parameter scaling
5. Conclude with transfer learning challenges specific to legal domain

### 3. Domain-Specific Models and Adaptation

#### Strengths:
- Good focus on specialized legal models
- Appropriate comparative framework

#### Areas for Improvement:
- Need more detailed evaluation metrics
- Should expand adaptation techniques

#### Writing Guidelines:
1. Start with comprehensive overview of legal domain challenges from Paper 3
2. Present AraLegal-BERT case study (Paper 1):
   - Training methodology
   - Adaptation techniques
   - Performance metrics
3. Analyze scaling benefits from Paper 13:
   - Parameter efficiency
   - Zero-shot capabilities
4. Include clear comparison tables showing:
   - Model architectures
   - Training approaches
   - Performance metrics

### 4. Multilingual and Cross-lingual Approaches

#### Strengths:
- Good coverage of multilingual capabilities
- Appropriate paper selection

#### Areas for Improvement:
- Need more legal-specific examples
- Should include performance metrics

#### Writing Guidelines:
1. Begin with mT5 architecture analysis (Paper 18):
   - Multilingual training approach
   - Cross-lingual transfer capabilities
2. Analyze BLOOM's multilingual capabilities (Paper 15):
   - Language coverage
   - Zero-shot performance
3. Include cross-lingual generalization (Paper 8):
   - Multitask finetuning results
   - Language transfer effectiveness
4. Provide specific legal domain examples:
   - Cross-jurisdictional applications
   - Performance across languages

### 5. Prompting and Task Adaptation

#### Strengths:
- Good coverage of modern techniques
- Clear application focus

#### Areas for Improvement:
- Need more legal-specific examples
- Should include failure cases

#### Writing Guidelines:
1. Begin with PromptSource framework (Paper 2):
   - Template design principles
   - Task adaptation methodology
2. Analyze zero-shot capabilities (Paper 14):
   - Prompt engineering techniques
   - Performance metrics
3. Include text classification specifics (Paper 16):
   - CARP methodology
   - Performance analysis
4. Provide legal-specific examples:
   - Prompt templates
   - Task adaptation cases

### 6. Applications and Implementation

#### Strengths:
- Good practical focus
- Clear implementation framework

#### Areas for Improvement:
- Need more technical details
- Should include system architecture

#### Writing Guidelines:
1. Start with public affairs classification (Paper 10):
   - System architecture
   - Implementation details
   - Performance metrics
2. Analyze legal case entailment (Paper 13):
   - Zero-shot approaches
   - Scaling effects
3. Include text classification framework (Paper 16):
   - CARP methodology
   - Real-world results
4. Provide detailed implementation guidelines:
   - System requirements
   - Performance optimization
   - Deployment considerations

### 7. Legal Alignment and Ethical Considerations

#### Strengths:
- Good coverage of critical issues
- Appropriate ethical focus

#### Areas for Improvement:
- Need more technical alignment details
- Should include bias metrics

#### Writing Guidelines:
1. Begin with legal informatics approach (Paper 9):
   - Alignment principles
   - Implementation framework
2. Analyze bias considerations (Paper 6):
   - Detection methods
   - Mitigation strategies
3. Include regulatory framework from Paper 7:
   - Compliance requirements
   - Implementation guidelines
4. Provide concrete recommendations:
   - Bias testing protocols
   - Alignment metrics

### 8. Future Directions and Challenges

#### Strengths:
- Good coverage of open problems
- Clear research directions

#### Areas for Improvement:
- Need more specific research questions
- Should include timeline estimates

#### Writing Guidelines:
1. Begin with current challenges from Paper 3:
   - Technical limitations
   - Data constraints
2. Analyze future directions from Paper 7:
   - Research opportunities
   - Development needs
3. Include BLOOM insights (Paper 15):
   - Scaling challenges
   - Resource requirements
4. Provide specific research recommendations:
   - Short-term goals
   - Long-term objectives

## General Writing Requirements

1. Technical Precision:
   - Use consistent terminology
   - Define all technical terms
   - Provide mathematical formulations where appropriate

2. Comparative Analysis:
   - Include comparison tables
   - Present performance metrics
   - Analyze trade-offs

3. Citation Standards:
   - Use consistent citation format
   - Cite all claims
   - Include page numbers for direct quotes

4. Visual Elements:
   - Include architecture diagrams
   - Present performance graphs
   - Use comparison tables

5. Writing Style:
   - Maintain academic tone
   - Use clear, concise language
   - Ensure logical flow between sections

## Final Notes

1. Each section must explicitly connect to the core papers listed
2. Avoid speculation beyond paper contents
3. Maintain consistent technical depth
4. Include clear transition paragraphs between sections
5. Ensure all claims are supported by paper citations

"""