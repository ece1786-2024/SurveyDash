import json
import pyperclip

from step3_get_revision_prompt import output as output3
from step4_get_advice_prompt import output as output4


def get_prompt(section, outline, feedback):
    with open(f'{file}.json', 'r') as f:
        data = json.load(f)

    abstracts = ""
    for i, d in enumerate(data):
        abstract = d['abstract'].replace("\n", ' ')
        abstracts += f"{i + 1}\n{d['title']}\n{abstract}\n\n"

    text = f"""You are a experienced professor preparing a survey paper. You have written the outline of the survey paper based on the papers you’ve read. You asked your colleague to review the outline and provide feedback. You should consider the feedback and start writing only the {section} section of the survey paper.

You must only write the {section} section you planned to write. Do not write the entire survey paper before making sure the current section is well-written. Your writing should be based on the outline you have created and the feedback you received.

Think step by step. Write comprehensive subsections and detailed contents based on the papers you have read. You are encouraged to compare and combine the data across different papers related to the topic to enrich the content. Do not make up any content that is not included in the abstracts of the papers. You must cite the papers in your writing. The citation should be consistent in this format: [index of the paper].

# Papers You Have Read

{abstracts}

# Outline of the Survey Paper

{outline}

# Feedback from Colleague

{feedback}

# {section} Section

"""

    return text


file = 'The_Impact_of_Large_Language_Modeling_on_Natural_Language_Processing_in_Legal_Texts_A_Comprehensive_Survey.pdf'
# file = 'The_Recent_Large_Language_Models_in_NLP.pdf'
# file = 'Multimodal_Large_Language_Models_A_Survey.pdf'

if __name__ == '__main__':
    pyperclip.copy(get_prompt(
        section='Pre-trained Language Models for Legal Texts',
        outline=output3, feedback=output4),
    )

output = """
## Pre-trained Language Models for Legal Texts

The emergence and refinement of pre-trained language models, such as BERT, have initiated a paradigm shift in natural language processing (NLP) by offering remarkable capabilities in understanding and generating human language. Within the specific realm of legal texts, which are replete with intricate terminologies and nuanced meanings, the adaptation of these models has been both a challenge and an opportunity. In this section, we delve into the specialized pre-trained language models designed for legal text analysis, assessing their effectiveness and comparing them to traditional models.

### Legal Domain-Specific Pre-trained Models

AraLegal-BERT is a noteworthy example of a domain-specific model fine-tuned for Arabic legal texts. This model is grounded in the architecture of BERT, a bidirectional encoder transformer that captures context-rich representations by conditioning on both the left and right contexts in all layers [4]. The AraLegal-BERT model is distinctive because it is tailored specifically to handle the complexities of legal documentation in the Arabic language [1]. Tests conducted have demonstrated that AraLegal-BERT outperforms its general-purpose counterparts, achieving better accuracy in legal text processing and comprehension tasks [1].

Another study examined 12 legal-domain-specific pre-trained models across different languages and legal frameworks [3]. This investigation highlighted the prominence of pre-trained models in enhancing the accuracy of predicting legal judgments from complex factual descriptions, illustrating the broad utility of these models in multilingual contexts. The findings underscored that domain-specific pre-training significantly boosts performance metrics across various legal tasks, underscoring the model's adaptability to legal jargon and phraseology.

### Comparison with Traditional Models

Traditional pre-trained models, particularly the original BERT, have set a benchmark in many NLP applications. However, when benchmarked against models like AraLegal-BERT, conventional BERT demonstrates limitations in handling legal texts which are often unique in structure and content [1]. While BERT excels in general language understanding, legal texts' specialized vocabulary and syntax necessitate tailored pre-training to capture the subtleties present in legal documents effectively.

The comparative analysis revealed that models specifically trained on legal datasets, such as those utilized in Legal Judgment Prediction tasks, provide more accurate and context-aware judgments [3]. These models leverage large-scale legal datasets, offering refined capabilities in jurisdictions and interpreting legal statutes and precedents more effectively than traditional, broad-spectrum language models [3].

### Dataset Utilization and Efficacy

Effective pre-training hinges on leveraging relevant and comprehensive datasets. The AraLegal-BERT development process involved using domain-relevant training and testing datasets to fine-tune the model, ensuring it aligns well with the lexical and syntactical demands of legal Arabic texts [1]. Similarly, paper 3 emphasizes the criticality of large-scale, diverse datasets that span various legal systems to enhance model robustness and linguistic coverage.

A significant challenge in developing these models lies in the diversity of legal frameworks and languages. While existing datasets provide a foundational corpus for model training, the linguistic and legal variability necessitate ongoing expansion and adaptation of these datasets to maintain and augment model efficacy [3, 5].

### Regional and Linguistic Performance

The performance of pre-trained language models in legal contexts varies significantly across different linguistic and regional settings. AraLegal-BERT, for instance, demonstrates superior performance within Arabic jurisdictions due to its focused pre-training regimen [1]. However, this specificity also presents a limitation when attempting to generalize across different legal systems or languages lacking targeted models.

In broader multilingual assessments, models trained on diverse datasets offer robust zero-shot capabilities, extending their utility beyond initially intended languages and legal systems [3, 15]. This adaptability showcases the promise of multilingual pre-training for extrapolating learned insights across varied legal contexts, thus bridging regional and linguistic divides.

### Conclusion

Pre-trained language models tailored for legal texts, such as AraLegal-BERT, offer significant advancements over traditional models by enhancing the accuracy and efficiency of legal document processing. The critical role of targeted datasets and domain-specific pre-training cannot be understated, as they directly influence the model's effectiveness in dealing with the complexities of legal language. As the legal field continues to explore and refine these applications, expanding models to accommodate diverse legal frameworks and languages will be pivotal in realizing the full potential of AI in legal contexts.
"""
