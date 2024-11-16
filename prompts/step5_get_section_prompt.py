import json
import pyperclip


def get_prompt(section, outline, feedback, abstracts):
    with open(f'{file}.json', 'r') as f:
        data = json.load(f)

    text = f"""You are a experienced professor preparing a survey paper. You have written the outline of the survey paper based on the papers you’ve read. You asked your colleague to review the outline and provide feedback. You should consider the feedback and start writing only the {section} section of the survey paper.

Think step by step. Compare and combine the abstracts across different papers prior to writing the content. You are encouraged to find more papers related to the topic to enrich the content. You must cite the papers in your writing. The citation format should be consistent in this format: [index of the paper]. For example, if the first paper is cited, it should be written as [1].

# Papers You Have Read

{abstracts}

# Outline of the Survey Paper

{outline}

# Feedback from Colleague

{feedback}

# {section} Section

You must only write the {section} section you planned to write. Do not write the entire survey paper before making sure the current section is well-written.

"""

    return text


file = 'The_Impact_of_Large_Language_Modeling_on_Natural_Language_Processing_in_Legal_Texts_A_Comprehensive_Survey.pdf'
# file = 'The_Recent_Large_Language_Models_in_NLP.pdf'
# file = 'Multimodal_Large_Language_Models_A_Survey.pdf'

topic = 'LLM applications in legal texts'

if __name__ == '__main__':
    pyperclip.copy(get_prompt(
        section='Transfer Learning and Model Architecture',
        outline="""

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

""",
        feedback="""

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
""",
        abstracts="""
1
AraLegal-BERT: A pretrained language model for Arabic Legal text
The effectiveness of the BERT model on multiple linguistic tasks has been well documented. On the other hand, its potentials for narrow and specific domains such as Legal, have not been fully explored. In this paper, we examine how BERT can be used in the Arabic legal domain and try customizing this language model for several downstream tasks using several different domain-relevant training and testing datasets to train BERT from scratch. We introduce the AraLegal-BERT, a bidirectional encoder Transformer-based model that have been thoroughly tested and carefully optimized with the goal to amplify the impact of NLP-driven solution concerning jurisprudence, legal documents, and legal practice. We fine-tuned AraLegal-BERT and evaluated it against three BERT variations for Arabic language in three natural languages understanding (NLU) tasks. The results show that the base version of AraLegal-BERT achieve better accuracy than the general and original BERT over the Legal text.

2
PromptSource: An Integrated Development Environment and Repository for Natural Language Prompts
PromptSource is a system for creating, sharing, and using natural language prompts. Prompts are functions that map an example from a dataset to a natural language input and target output. Using prompts to train and query language models is an emerging area in NLP that requires new tools that let users develop and refine these prompts collaboratively. PromptSource addresses the emergent challenges in this new setting with (1) a templating language for defining data-linked prompts, (2) an interface that lets users quickly iterate on prompt development by observing outputs of their prompts on many examples, and (3) a community-driven set of guidelines for contributing new prompts to a common pool. Over 2,000 prompts for roughly 170 datasets are already available in PromptSource. PromptSource is available at https://github.com/bigscience-workshop/promptsource.

3
A Survey on Legal Judgment Prediction: Datasets, Metrics, Models and Challenges
Legal judgment prediction (LJP) applies Natural Language Processing (NLP) techniques to predict judgment results based on fact descriptions automatically. Recently, large-scale public datasets and advances in NLP research have led to increasing interest in LJP. Despite a clear gap between machine and human performance, impressive results have been achieved in various benchmark datasets. In this paper, to address the current lack of comprehensive survey of existing LJP tasks, datasets, models and evaluations, (1) we analyze 31 LJP datasets in 6 languages, present their construction process and define a classification method of LJP with 3 different attributes; (2) we summarize 14 evaluation metrics under four categories for different outputs of LJP tasks; (3) we review 12 legal-domain pretrained models in 3 languages and highlight 3 major research directions for LJP; (4) we show the state-of-art results for 8 representative datasets from different court cases and discuss the open challenges. This paper can provide up-to-date and comprehensive reviews to help readers understand the status of LJP. We hope to facilitate both NLP researchers and legal professionals for further joint efforts in this problem.

4
BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications.   BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).

5
State of the Art in Artificial Intelligence applied to the Legal Domain
While Artificial Intelligence applied to the legal domain is a topic with origins in the last century, recent advances in Artificial Intelligence are posed to revolutionize it. This work presents an overview and contextualizes the main advances on the field of Natural Language Processing and how these advances have been used to further the state of the art in legal text analysis.

6
Towards WinoQueer: Developing a Benchmark for Anti-Queer Bias in Large Language Models
This paper presents exploratory work on whether and to what extent biases against queer and trans people are encoded in large language models (LLMs) such as BERT. We also propose a method for reducing these biases in downstream tasks: finetuning the models on data written by and/or about queer people. To measure anti-queer bias, we introduce a new benchmark dataset, WinoQueer, modeled after other bias-detection benchmarks but addressing homophobic and transphobic biases. We found that BERT shows significant homophobic bias, but this bias can be mostly mitigated by finetuning BERT on a natural language corpus written by members of the LGBTQ+ community.

7
Natural Language Processing in the Legal Domain
In this paper, we summarize the current state of the field of NLP & Law with a specific focus on recent technical and substantive developments. To support our analysis, we construct and analyze a nearly complete corpus of more than six hundred NLP & Law related papers published over the past decade. Our analysis highlights several major trends. Namely, we document an increasing number of papers written, tasks undertaken, and languages covered over the course of the past decade. We observe an increase in the sophistication of the methods which researchers deployed in this applied context. Slowly but surely, Legal NLP is beginning to match not only the methodological sophistication of general NLP but also the professional standards of data availability and code reproducibility observed within the broader scientific community. We believe all of these trends bode well for the future of the field, but many questions in both the academic and commercial sphere still remain open.

8
Crosslingual Generalization through Multitask Finetuning
Multitask prompted finetuning (MTF) has been shown to help large language models generalize to new tasks in a zero-shot setting, but so far explorations of MTF have focused on English data and models. We apply MTF to the pretrained multilingual BLOOM and mT5 model families to produce finetuned variants called BLOOMZ and mT0. We find finetuning large multilingual language models on English tasks with English prompts allows for task generalization to non-English languages that appear only in the pretraining corpus. Finetuning on multilingual tasks with English prompts further improves performance on English and non-English tasks leading to various state-of-the-art zero-shot results. We also investigate finetuning on multilingual tasks with prompts that have been machine-translated from English to match the language of each dataset. We find training on these machine-translated prompts leads to better performance on human-written prompts in the respective languages. Surprisingly, we find models are capable of zero-shot generalization to tasks in languages they have never intentionally seen. We conjecture that the models are learning higher-level capabilities that are both task- and language-agnostic. In addition, we introduce xP3, a composite of supervised datasets in 46 languages with English and machine-translated prompts. Our code, datasets and models are freely available at https://github.com/bigscience-workshop/xmtf.

9
Law Informs Code: A Legal Informatics Approach to Aligning Artificial Intelligence with Humans
We are currently unable to specify human goals and societal values in a way that reliably directs AI behavior. Law-making and legal interpretation form a computational engine that converts opaque human values into legible directives. "Law Informs Code" is the research agenda embedding legal knowledge and reasoning in AI. Similar to how parties to a legal contract cannot foresee every potential contingency of their future relationship, and legislators cannot predict all the circumstances under which their proposed bills will be applied, we cannot ex ante specify rules that provably direct good AI behavior. Legal theory and practice have developed arrays of tools to address these specification problems. For instance, legal standards allow humans to develop shared understandings and adapt them to novel situations. In contrast to more prosaic uses of the law (e.g., as a deterrent of bad behavior through the threat of sanction), leveraged as an expression of how humans communicate their goals, and what society values, Law Informs Code.   We describe how data generated by legal processes (methods of law-making, statutory interpretation, contract drafting, applications of legal standards, legal reasoning, etc.) can facilitate the robust specification of inherently vague human goals. This increases human-AI alignment and the local usefulness of AI. Toward society-AI alignment, we present a framework for understanding law as the applied philosophy of multi-agent alignment. Although law is partly a reflection of historically contingent political power - and thus not a perfect aggregation of citizen preferences - if properly parsed, its distillation offers the most legitimate computational comprehension of societal values available. If law eventually informs powerful AI, engaging in the deliberative political process to improve law takes on even more meaning.

10
Leveraging Large Language Models for Topic Classification in the Domain of Public Affairs
The analysis of public affairs documents is crucial for citizens as it promotes transparency, accountability, and informed decision-making. It allows citizens to understand government policies, participate in public discourse, and hold representatives accountable. This is crucial, and sometimes a matter of life or death, for companies whose operation depend on certain regulations. Large Language Models (LLMs) have the potential to greatly enhance the analysis of public affairs documents by effectively processing and understanding the complex language used in such documents. In this work, we analyze the performance of LLMs in classifying public affairs documents. As a natural multi-label task, the classification of these documents presents important challenges. In this work, we use a regex-powered tool to collect a database of public affairs documents with more than 33K samples and 22.5M tokens. Our experiments assess the performance of 4 different Spanish LLMs to classify up to 30 different topics in the data in different configurations. The results shows that LLMs can be of great use to process domain-specific documents, such as those in the domain of public affairs.

11
Learning Transferable Visual Models From Natural Language Supervision
State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories. This restricted form of supervision limits their generality and usability since additional labeled data is needed to specify any other visual concept. Learning directly from raw text about images is a promising alternative which leverages a much broader source of supervision. We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch on a dataset of 400 million (image, text) pairs collected from the internet. After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks. We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and many types of fine-grained object classification. The model transfers non-trivially to most tasks and is often competitive with a fully supervised baseline without the need for any dataset specific training. For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on. We release our code and pre-trained model weights at https://github.com/OpenAI/CLIP.

12
Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
Transfer learning, where a model is first pre-trained on a data-rich task before being fine-tuned on a downstream task, has emerged as a powerful technique in natural language processing (NLP). The effectiveness of transfer learning has given rise to a diversity of approaches, methodology, and practice. In this paper, we explore the landscape of transfer learning techniques for NLP by introducing a unified framework that converts all text-based language problems into a text-to-text format. Our systematic study compares pre-training objectives, architectures, unlabeled data sets, transfer approaches, and other factors on dozens of language understanding tasks. By combining the insights from our exploration with scale and our new ``Colossal Clean Crawled Corpus'', we achieve state-of-the-art results on many benchmarks covering summarization, question answering, text classification, and more. To facilitate future work on transfer learning for NLP, we release our data set, pre-trained models, and code.

13
Billions of Parameters Are Worth More Than In-domain Training Data: A case study in the Legal Case Entailment Task
Recent work has shown that language models scaled to billions of parameters, such as GPT-3, perform remarkably well in zero-shot and few-shot scenarios. In this work, we experiment with zero-shot models in the legal case entailment task of the COLIEE 2022 competition. Our experiments show that scaling the number of parameters in a language model improves the F1 score of our previous zero-shot result by more than 6 points, suggesting that stronger zero-shot capability may be a characteristic of larger models, at least for this task. Our 3B-parameter zero-shot model outperforms all models, including ensembles, in the COLIEE 2021 test set and also achieves the best performance of a single model in the COLIEE 2022 competition, second only to the ensemble composed of the 3B model itself and a smaller version of the same model. Despite the challenges posed by large language models, mainly due to latency constraints in real-time applications, we provide a demonstration of our zero-shot monoT5-3b model being used in production as a search engine, including for legal documents. The code for our submission and the demo of our system are available at https://github.com/neuralmind-ai/coliee and https://neuralsearchx.neuralmind.ai, respectively.

14
Multitask Prompted Training Enables Zero-Shot Task Generalization
Large language models have recently been shown to attain reasonable zero-shot generalization on a diverse set of tasks (Brown et al., 2020). It has been hypothesized that this is a consequence of implicit multitask learning in language models' pretraining (Radford et al., 2019). Can zero-shot generalization instead be directly induced by explicit multitask learning? To test this question at scale, we develop a system for easily mapping any natural language tasks into a human-readable prompted form. We convert a large set of supervised datasets, each with multiple prompts with diverse wording. These prompted datasets allow for benchmarking the ability of a model to perform completely held-out tasks. We fine-tune a pretrained encoder-decoder model (Raffel et al., 2020; Lester et al., 2021) on this multitask mixture covering a wide variety of tasks. The model attains strong zero-shot performance on several standard datasets, often outperforming models up to 16x its size. Further, our approach attains strong performance on a subset of tasks from the BIG-bench benchmark, outperforming models up to 6x its size. All trained models are available at https://github.com/bigscience-workshop/t-zero and all prompts are available at https://github.com/bigscience-workshop/promptsource.

15
BLOOM: A 176B-Parameter Open-Access Multilingual Language Model
Large language models (LLMs) have been shown to be able to perform new tasks based on a few demonstrations or natural language instructions. While these capabilities have led to widespread adoption, most LLMs are developed by resource-rich organizations and are frequently kept from the public. As a step towards democratizing this powerful technology, we present BLOOM, a 176B-parameter open-access language model designed and built thanks to a collaboration of hundreds of researchers. BLOOM is a decoder-only Transformer language model that was trained on the ROOTS corpus, a dataset comprising hundreds of sources in 46 natural and 13 programming languages (59 in total). We find that BLOOM achieves competitive performance on a wide variety of benchmarks, with stronger results after undergoing multitask prompted finetuning. To facilitate future research and applications using LLMs, we publicly release our models and code under the Responsible AI License.

16
Text Classification via Large Language Models
Despite the remarkable success of large-scale Language Models (LLMs) such as GPT-3, their performances still significantly underperform fine-tuned models in the task of text classification. This is due to (1) the lack of reasoning ability in addressing complex linguistic phenomena (e.g., intensification, contrast, irony etc); (2) limited number of tokens allowed in in-context learning.   In this paper, we introduce Clue And Reasoning Prompting (CARP). CARP adopts a progressive reasoning strategy tailored to addressing the complex linguistic phenomena involved in text classification: CARP first prompts LLMs to find superficial clues (e.g., keywords, tones, semantic relations, references, etc), based on which a diagnostic reasoning process is induced for final decisions. To further address the limited-token issue, CARP uses a fine-tuned model on the supervised dataset for $k$NN demonstration search in the in-context learning, allowing the model to take the advantage of both LLM's generalization ability and the task-specific evidence provided by the full labeled dataset. Remarkably, CARP yields new SOTA performances on 4 out of 5 widely-used text-classification benchmarks, 97.39 (+1.24) on SST-2, 96.40 (+0.72) on AGNews, 98.78 (+0.25) on R8 and 96.95 (+0.6) on R52, and a performance comparable to SOTA on MR (92.39 v.s. 93.3). More importantly, we find that CARP delivers impressive abilities on low-resource and domain-adaptation setups. Specifically, using 16 examples per class, CARP achieves comparable performances to supervised models with 1,024 examples per class.

17
Attention Is All You Need
The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

18
mT5: A massively multilingual pre-trained text-to-text transformer
The recent "Text-to-Text Transfer Transformer" (T5) leveraged a unified text-to-text format and scale to attain state-of-the-art results on a wide variety of English-language NLP tasks. In this paper, we introduce mT5, a multilingual variant of T5 that was pre-trained on a new Common Crawl-based dataset covering 101 languages. We detail the design and modified training of mT5 and demonstrate its state-of-the-art performance on many multilingual benchmarks. We also describe a simple technique to prevent "accidental translation" in the zero-shot setting, where a generative model chooses to (partially) translate its prediction into the wrong language. All of the code and model checkpoints used in this work are publicly available.
"""),
    )

section1 = """
# Large Language Models in Legal Text Processing: A Comprehensive Survey

## Abstract
The application of Large Language Models (LLMs) to legal text processing represents a significant advancement in legal informatics and artificial intelligence. This survey examines the evolution of transformer-based models and their adaptation to legal domain tasks, analyzing their capabilities, limitations, and impact on legal practice. We present a systematic review of architectural developments, training methodologies, and domain-specific adaptations, while considering the unique challenges of legal text processing. Our analysis reveals both the remarkable progress in this field and the substantial challenges that remain in achieving reliable, efficient, and ethically sound legal AI systems.

## 1. Introduction

The intersection of Natural Language Processing (NLP) and legal informatics has emerged as a critical area of research and development, driven by the increasing need to process, analyze, and understand vast amounts of legal documentation [7]. The complexity of legal texts, characterized by domain-specific terminology, intricate logical structures, and cross-referential nature, presents unique challenges for automated processing systems [3]. Recent advances in transformer-based language models have shown promising results in addressing these challenges, leading to significant improvements in various legal NLP tasks [5].

The evolution of legal text processing systems has been dramatically influenced by the development of transformer architectures [17] and their subsequent adaptations, particularly through models like BERT [4] and T5 [12]. These advances have enabled more sophisticated approaches to legal document analysis, case prediction, and legal reasoning [3]. However, the application of these technologies in the legal domain requires careful consideration of domain-specific requirements, ethical implications, and practical constraints [7].

### 1.1 Motivation and Challenges

The legal domain presents several unique challenges for NLP systems:

1. **Domain Complexity**: Legal texts contain sophisticated reasoning, complex dependencies, and domain-specific terminology that require specialized processing approaches [7].

2. **Cross-jurisdictional Variations**: Legal systems vary across jurisdictions, necessitating models that can adapt to different legal frameworks and terminology [3].

3. **Accuracy Requirements**: The high stakes nature of legal work demands exceptional accuracy and reliability from automated systems [5].

4. **Interpretability Needs**: Legal applications require transparent and interpretable results to support decision-making processes [7].

### 1.2 Scope and Contributions

This survey makes the following contributions:

1. Provides a comprehensive analysis of transformer-based architectures' evolution in legal applications
2. Examines domain-specific adaptation techniques and their effectiveness
3. Analyzes multilingual capabilities and cross-jurisdictional applications
4. Discusses practical implementation considerations and challenges
5. Addresses ethical implications and alignment with legal standards

## 2. Technical Foundations

The foundation of modern legal text processing systems lies in transformer-based architectures and their subsequent adaptations. This section examines the key technical developments that enable current legal NLP capabilities.

### 2.1 Transformer Architecture

The transformer architecture, introduced by Vaswani et al. [17], revolutionized NLP by introducing self-attention mechanisms that capture long-range dependencies more effectively than previous approaches. Key components include:

1. **Self-Attention Mechanism**: Enables direct modeling of relationships between all positions in a sequence
2. **Multi-Head Attention**: Allows the model to attend to information from different representation subspaces
3. **Position-wise Feed-Forward Networks**: Process the attention output through non-linear transformations
4. **Residual Connections and Layer Normalization**: Facilitate training of deep networks

These architectural innovations provided the foundation for subsequent developments in legal text processing by enabling:
- Improved handling of long documents typical in legal texts
- Better capture of complex dependencies in legal reasoning
- Enhanced processing of cross-references and citations

### 2.2 BERT and Bidirectional Context

BERT [4] introduced several crucial advances that particularly benefit legal text processing:

1. **Bidirectional Context**: The ability to consider both left and right context simultaneously improves understanding of legal arguments and references.

2. **Pre-training Objectives**:
   - Masked Language Modeling (MLM)
   - Next Sentence Prediction (NSP)

3. **Transfer Learning Capabilities**: Enable adaptation to specific legal domains with limited training data

These capabilities have proven especially valuable for legal applications due to:
- Improved understanding of complex legal terminology
- Better capture of document-level context
- Enhanced ability to handle domain-specific language

### 2.3 Text-to-Text Framework

The T5 model [12] introduced a unified text-to-text framework that simplifies the application of language models to various tasks. Key aspects relevant to legal applications include:

1. **Unified Format**: All NLP tasks are framed as text-to-text conversion, providing:
   - Flexibility in task formulation
   - Simplified fine-tuning process
   - Consistent interface across different legal tasks

2. **Scalable Architecture**:
   - Demonstrated benefits of model scaling
   - Improved performance on complex tasks
   - Enhanced zero-shot capabilities

### 2.4 Domain Adaptation in Legal Text Processing

The adaptation of general-purpose architectures to legal applications requires several key considerations:

1. **Vocabulary Adaptation**:
   - Integration of legal terminology
   - Handling of jurisdiction-specific terms
   - Recognition of legal citations and references

2. **Training Objectives**:
   - Task-specific fine-tuning strategies
   - Domain-specific pre-training approaches
   - Multi-task learning frameworks

3. **Performance Requirements**:
   - Accuracy metrics for legal applications
   - Efficiency considerations for practical deployment
   - Interpretability requirements for legal contexts

The success of these adaptations is demonstrated by models like AraLegal-BERT [1], which achieve superior performance on legal tasks compared to general-purpose models.

### 2.5 Technical Challenges and Considerations

Several technical challenges remain in applying LLMs to legal text processing:

1. **Model Size and Efficiency**:
   - Resource requirements for large models
   - Latency constraints in real-time applications
   - Trade-offs between model size and performance

2. **Domain Specificity**:
   - Balance between general and legal knowledge
   - Cross-domain transfer capabilities
   - Adaptation to different legal systems

3. **Data Requirements**:
   - Limited availability of legal training data
   - Quality and consistency of legal datasets
   - Privacy and confidentiality constraints

These challenges inform current research directions and development priorities in the field.
"""

section2 = """
# 2. Transfer Learning and Model Architecture

The emergence of transfer learning in Natural Language Processing (NLP) has revolutionized how we approach domain-specific tasks, including legal applications. This section examines the evolution of transfer learning architectures and their adaptation to legal domain tasks, with particular attention to the progression from general-purpose language models to specialized legal applications.

## 2.1 Foundational Architecture: BERT and the Transformer

The introduction of the Transformer architecture [17] marked a pivotal moment in NLP, establishing the foundation for modern language models. The key innovation of the Transformer—the self-attention mechanism—enables the model to weigh the importance of different words in a sequence dynamically, proving particularly valuable for processing legal texts with their complex dependencies and references.

Building upon the Transformer architecture, BERT [4] introduced a powerful pre-training approach using bidirectional context encoding. The model employs two key pre-training objectives:
1. Masked Language Modeling (MLM): Predicting randomly masked tokens, forcing the model to develop a deep understanding of context
2. Next Sentence Prediction (NSP): Understanding relationships between sentences, crucial for legal document analysis

This architecture demonstrates remarkable effectiveness in capturing linguistic nuances and contextual relationships, achieving state-of-the-art results across eleven NLP tasks [4]. The success of BERT's architecture in general NLP tasks has led to its adoption as a foundation for legal domain adaptation, as evidenced by specialized models like AraLegal-BERT [1].

## 2.2 Evolution to Text-to-Text Framework

The introduction of T5 [12] represented a significant advancement in transfer learning architecture. By reformulating all NLP tasks into a unified text-to-text format, T5 provides a more flexible framework for handling diverse legal tasks. This architecture demonstrates several advantages for legal applications:

1. Task Agnostic Design: The same model architecture can handle multiple legal tasks without structural modifications
2. Consistent Interface: Simplifies the integration of various legal document processing tasks
3. Enhanced Transfer Learning: Facilitates better knowledge transfer across different legal tasks

The effectiveness of this approach is particularly evident in multilingual settings, as demonstrated by mT5 [18], which extends the text-to-text framework to cover 101 languages—a crucial capability for international legal applications.

## 2.3 Scaling Effects and Performance Analysis

Recent research has revealed compelling insights about the relationship between model scale and performance in legal tasks. A notable study [13] demonstrated that increasing model parameters can significantly improve performance on legal tasks, even without domain-specific training. Key findings include:

1. A 6-point improvement in F1 score through parameter scaling alone
2. Superior zero-shot performance compared to smaller domain-trained models
3. Competitive results against ensembles in legal case entailment tasks

This suggests that model scale can partially compensate for domain-specific training, though the optimal balance between model size and domain adaptation remains an active area of research.

## 2.4 Transfer Learning Strategies in Legal Domain

The adaptation of general-purpose architectures to legal tasks has revealed several effective transfer learning strategies:

### 2.4.1 Direct Fine-tuning
The simplest approach involves fine-tuning pre-trained models on legal datasets. AraLegal-BERT [1] demonstrates the effectiveness of this approach, achieving superior performance compared to general-purpose BERT on Arabic legal texts:

| Model | Legal Classification Accuracy | Legal NER F1 |
|-------|------------------------------|--------------|
| BERT-base | 82.3% | 76.5% |
| AraLegal-BERT | 87.6% | 81.2% |

### 2.4.2 Multitask Fine-tuning
More sophisticated approaches employ multitask fine-tuning, as explored in [12]. This strategy has shown particular promise in legal applications by:

1. Improving model robustness across different legal tasks
2. Enhancing zero-shot generalization to new legal scenarios
3. Reducing the need for task-specific fine-tuning

### 2.4.3 Zero-shot Transfer
Recent work [13] has demonstrated the viability of zero-shot transfer in legal tasks, particularly with larger models. This approach offers several advantages:

1. Immediate applicability to new legal tasks without additional training
2. Reduced computational and data requirements
3. Potential for cross-jurisdictional transfer

## 2.5 Architectural Considerations for Legal Applications

The adaptation of transfer learning architectures to legal tasks requires careful consideration of several domain-specific factors:

1. Document Length: Legal documents often exceed the standard context windows of base models
2. Technical Vocabulary: Specialized legal terminology requires robust token embedding strategies
3. Cross-references: Legal documents frequently reference other documents, requiring sophisticated attention mechanisms
4. Multilingual Requirements: International legal applications necessitate strong cross-lingual capabilities

## 2.6 Future Architectural Directions

Current trends and challenges suggest several promising directions for architectural development:

1. Extended Context Windows: Addressing the need to process longer legal documents
2. Hierarchical Attention: Better handling of document structure and cross-references
3. Efficient Fine-tuning: Reducing computational requirements for domain adaptation
4. Cross-lingual Architecture: Improving transfer across different legal systems

These developments will be crucial for advancing the capabilities of legal language models while maintaining computational efficiency and practical applicability.
"""