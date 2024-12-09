import argparse
import os
import json

import download_abs
from refined_paper import gen_survey_outline


def download_and_parse(file):
    directory = os.path.dirname(file)
    file_name = os.path.basename(file)
    file_name = file_name.split('.')[0]
    data_file = f'{directory}/../abs/{file_name}.json'

    if not os.path.exists(data_file):
        download_abs.get_data(file)

    with open(data_file) as f:
        data = json.load(f)

    abstracts = ""
    for i, d in enumerate(data):
        abstract = d["abstract"].replace("\n", " ")
        abstracts += f"{i + 1}\n{d['title']}\n{abstract}\n\n"

    return abstracts


def survey_dash(topic, file):
    abstracts = download_and_parse(file)
    final_outline, section_list = gen_survey_outline(abstracts, topic)
    print(final_outline, section_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SurveyDash')
    parser.add_argument('-s', '--survey', required=True, help='Survey name')
    parser.add_argument('-p', '--papers', type=str, required=True, help='Path to the TXT file of paper titles')

    args = parser.parse_args()
    survey_dash(args.survey, args.papers)

"""
python main.py --survey "LLM applications in legal texts" --papers "dataset/txt/1.txt"
"""
