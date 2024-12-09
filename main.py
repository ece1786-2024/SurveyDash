import argparse
import os
import json

import pymupdf4llm

import download_abs
from refined_paper import (
    gen_survey_outline,
    read_and_summarize_articles,
    enrich_section,
)


def download_and_parse(file):
    directory = os.path.dirname(file)
    file_name = os.path.basename(file)
    file_name = file_name.split('.')[0]
    data_file = f'{directory}/../abs/{file_name}.json'
    pdf_dir = f'{directory}/../pdf/{file_name}'

    if not os.path.exists(data_file) or not os.path.exists(pdf_dir):
        download_abs.get_data(file)

    with open(data_file) as f:
        data = json.load(f)

    abstracts = ""
    for i, d in enumerate(data):
        abstract = d["abstract"].replace("\n", " ")
        abstracts += f"{i + 1}\n{d['title']}\n{abstract}\n\n"

    contents = {}
    for i, d in enumerate(data):
        curr_content = pymupdf4llm.to_markdown(f"{pdf_dir}/{d['title']}.pdf")
        contents[i + 1] = curr_content
    return abstracts, contents


def survey_dash(topic, file):
    abstracts, contents = download_and_parse(file)
    final_outline, section_list = gen_survey_outline(abstracts, topic)
    summaries = read_and_summarize_articles(contents)
    enrich_section(section_list, topic, final_outline, summaries)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SurveyDash')
    parser.add_argument('-s', '--survey', required=True, help='Survey name')
    parser.add_argument('-p', '--papers', type=str, required=True, help='Path to the TXT file of paper titles')

    args = parser.parse_args()
    survey_dash(args.survey, args.papers)

"""
python main.py --survey "LLM applications in legal texts" --papers "dataset/txt/1.txt"
"""
