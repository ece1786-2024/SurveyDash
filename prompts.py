_outline_generation_prompt = """
You are a experienced professor preparing a survey paper. Your task is to create a structured outline for the survey based on the papers you've read. This outline should help organize your analysis and highlight key themes.

## Outline the Structure

Divide your outline into thematic sections from introduction to conclusion. Each section should cover a main idea, group related papers, and outline how these studies contribute to your understanding of the topic.

## General Requirements

Think step by step. Compare and combine the abstracts across different papers prior to creating the outline. You must draft the outline of the survey paper only based on the given papers. Using content that are not included in the abstracts is strictly prohibited. 

## Outline Template

For each section, use the following template to include the following details:

1. [Title: Create a concise title that reflects the section's primary focus or theme.]
  - [Main Idea: Summarize the core concept or question that this section will address.]
  - [Core Papers: List the IDs of the papers relevant to this section. Write only indexes in the format: 1, 2, 3.]
  - [Possible Related Papers: List the IDs of the papers that could be relevant to this section. Write only indexes in the format: 1, 2, 3.]
  - [Content Structure: Briefly outline the content of the section, including: A summary of each paper's contributions. Comparisons or contrasts among the papers. Any gaps or unresolved issues identified in this group of papers.]
  - [Cohesion Across Sections: Consider adding notes on how sections connect to build a cohesive narrative for the review.]

# This time, you are focusing on the topic: {topic}.

## Papers

"""

_outline_revision_prompt = """
You are a experienced professor and are extremely demanding and expects perfection from your students. You are reviewing the outline of a survey paper created by a student. Your task is to provide constructive feedback on the outline to help the student improve the structure and content of the survey paper.

## General Requirements
1. You should make sure the student's outline is well-structured, coherent, and effectively conveys the main ideas and contributions of the selected papers. 
2. The student must mention all the core papers and all possible related papers in each section, but must not make up any content that is not included in the abstracts of the papers.
3. You must provide detailed feedback on the student's outline, highlighting areas for improvement and suggesting ways to enhance the clarity, coherence, and depth of the survey. Your feedback should be specific, actionable, and focused on guiding the student towards a more comprehensive and well-organized survey paper.

You will grade the student's outline. You are encouraged to provide detailed feedback to help the student revise and improve the outline effectively. Only give them a pass if the outline meets your high standards and expectations.

## Handout for Student's Outline Review

{prev_prompt}

## Student's Outline

{reply}

## Grade

- [ ] Pass
- [ ] Revision Needed
- [ ] Fail

## Feedback
"""

_outline_advice_prompt = """
You are a experienced professor and are extremely demanding and expects perfection from your students. You are reviewing the outline of a survey paper created by a student. Your task is to provide constructive feedback on the outline to help the student improve the structure and content of the survey paper.

## General Requirements
1. You should make sure the student's outline is well-structured, coherent, and effectively conveys the main ideas and contributions of the selected papers. 
2. The student must mention all the core papers and all possible related papers in each section, but must not make up any content that is not included in the abstracts of the papers.
3. The student hand back the revised outline to you and will proceed to write each section of the survey paper based on your next feedback. You must highlight areas for improvement and suggesting ways to enhance the clarity, coherence, and depth of the survey. 
4. Your feedback should be specific, actionable, and focused on guiding the student towards a more comprehensive and well-organized survey paper. Your feedback should be detailed and provide clear directions for the student to follow on writing each section.

# Handout for Student's Outline Review

{prev_prompt}

# Student's Outline

{reply}

# Feedback on revision

# Suggestions for writing each section
 
## General Requirements
"""

_section_outline_prompt = """
You are a experienced professor preparing a survey paper. You have written the outline of the survey paper based on the papers you’ve read. You asked your colleague to review the outline and provide feedback. You should consider the feedback and start writing only the {section} section of the survey paper.

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

_section_writer_prompt = """
## Role 
You are a researcher with expertise in writing academic survey papers 

## Objective 
You are tasked to enrich the current draft content for a subsection.

## Context 
1. You will be provided with a research paper, as well as its index number, that is relevant to the content of this subsection at a time as reference. The research paper provided has already been cited in the draft using the format [index of the paper]. 
2. You will be provided with the current draft of the section of the survey paper. The current draft of the section is written using only the abstract of the research paper. 

## Steps 
You **must** think step-by-step when writing the subsection. 
1. **Analyze** 
1-1. Analyze the content of the provided research paper. Specifically, you need to analyze what sections of the provided research paper is most relevant to the current subsection of the survey paper. Make sure you fully understand the content of the research paper before writing. 
1-2. Analyze the current draft of the subsection. Specifically, you need to check how you can enrich the content in the current draft using the content from the provided research paper. 
2. **Write**: write the draft of the subsection using **only** the content of the provided research paper. **Do not** modify parts that are not relevant to the content of the provided research paper. 
3. **Evaluate**: evaluate the draft you just created. 

## Requirement 
1. When writing the content, you **must** ensure you are only using the content of the provided research paper.
2. You **must** cite the paper when 
2-1. Summarizing Research: Cite sources when summarizing the existing literature. 
2-2. Using Specific Concepts or Data: Provide citations when discussing specific theories, models, or data. 
2-3. Comparing Findings: Cite relevant studies when comparing or contrasting different findings. 
2-4. Highlighting Research Gaps: Cite previous research when pointing out gaps your survey addresses. 
2-5. Using Established Methods: Cite the creators of methodologies you employ in your survey. 
2-6. Supporting Arguments: Cite sources that back up your conclusions and arguments. 
2-7. Suggesting Future Research: Reference studies related to proposed future research directions. 
3. Whenever information from the provided contexts is used or referenced, you **must** cite it appropriately using the format [x], where x is the index number of the paper. If a sentence comes from multiple contexts, please list **all** applicable citations, like [x_1; x_2]. You **do not** need to provide a separate section for reference in your response. 
3-1. If you are modifying an existing sentence in the draft that already contains a citation, **do not** delete this citation when modifying. 
3-2. Citation Example: the emergence of large language models (LLMs) [1] 
4. The draft for the subsection **must** be less than 1000 words. 
5. Do not report your thought process, return the draft only. 

# The topic of the survey paper is: {topic}
# The current section you are working on is: {section}.

You must only write the {section} section you planned to write. Do not write the entire survey paper before making sure the current section is well-written.


## Outline
{outline}

## Papers
"""


_section_advice_prompt = """
    The following are two sections from a rough draft of a survey paper. You are acting as an editor before the author can publish their paper.
    Provide suggestions on improving the quality of these sections. Find places that are repetitive, where not enough detail is provided, or ideas that can be combined to make the sections more concise.
    You are not limited to these types of suggestions. For each suggestion, clearly state what needs to be modified and how it should be modified. Also, list out your reasons for each modification:

    Section 1:
    {section1}

    Section 2:
    {section2}
    """
    
    
_section_refine_prompt = """
    You are the author of the survey paper, and you are doing your final edits before submitting the paper to a conference. There are suggestion provided by editors. You need to follow the suggestions to modify your paper or your paper will not be accepted by the conference. You also need to write the final paper in a formal format of a survey paper. You would submit this draft to the conference. It is also important to note that the writings provided to you is only a part of the survey paper. You should edit the writing according to the section title only. You also need to provide numbered sections. Ignore the context in your memory from previous chats. Make sure you only use the information from this prompt. It is important to note that the following writing is only part of the survey paper. Do not treat it as an entire survey paper.
    Section 1:
    {section1}

    Section 2:
    {section2}
    
    ## Suggestions
    """