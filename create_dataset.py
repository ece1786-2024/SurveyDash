import argparse
import re
import random
from pypdf import PdfReader


def extract_references(pdf_path, last_page=-1, sep='.'):
    reader = PdfReader(pdf_path)

    # print the number of pages in pdf file
    print(len(reader.pages), "pages")

    references = ''

    while last_page < 0:
        references += reader.pages[last_page].extract_text()
        last_page += 1

    references = references.replace('-\n', '').replace('\n', ' ').split('[')

    titles = []
    index = 1

    for reference in references:
        if not reference.startswith(f"{index}]"):
            continue

        title = ''
        try:
            if sep == '“':
                if '“' in reference:
                    title = reference.split('“')[1]
                    title = title.split('”')[0]
                else:
                    title = reference.split('"')[1]
            else:
                i, r = 1, reference.split('.')
                while True:
                    title = r[i]
                    if len(title) > 25 and 'et al' not in title:
                        break
                    i += 1

        except Exception as e:
            print(e)
            # input(reference)

        title = re.sub(r'[^a-zA-Z0-9 -]', '', title.strip())
        print(reference)
        print(index, title)

        if title:
            titles.append(title)
        index += 1

    return titles


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract references papers from a PDF file')

    parser.add_argument('--name', type=str, required=True, help='Name of the TXT file')
    parser.add_argument('--file', type=str, required=True, help='Path to the PDF file')
    parser.add_argument('--pages', type=int, default=1, help='Number of reference pages to extract')
    parser.add_argument('--sep', type=str, default='.', help='Separator: “ or .')

    args = parser.parse_args()

    papers = extract_references('./dataset/pdf/' + args.file, last_page=-args.pages, sep=args.sep)
    # random.shuffle(papers)

    with open(f'./dataset/txt/{args.name}.txt', 'w') as f:
        f.write('\n'.join(papers))

"""
# Usage
python create_dataset.py --name 1 --file The_Impact_of_Large_Language_Modeling_on_Natural_Language_Processing_in_Legal_Texts_A_Comprehensive_Survey.pdf --pages 1 --sep .
python create_dataset.py --name 2 --file The_Recent_Large_Language_Models_in_NLP.pdf --pages 1 --sep “
python create_dataset.py --name 3 --file Multimodal_Large_Language_Models_A_Survey.pdf --pages 2 --sep “
python create_dataset.py --name 4 --file 2212.10609v1.pdf --pages 5 --sep .
"""
