import json
import re
from pypdf import PdfReader
import arxiv


def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2 + 1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


def search_by_title(title, max_results=10):
    search = arxiv.Search(
        query="ti:" + title,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    return search.results()


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
                title = reference.split('.')[1]
                if len(title) < 25:
                    title = reference.split('.')[2]
        except Exception as e:
            print(e)
            # input(reference)

        title = re.sub(r'[^a-zA-Z0-9 -]', '', title.strip())
        print(reference)
        print(index, title)

        titles.append(title)
        index += 1

    return titles


def search_on_arxiv(titles):
    data = []

    for title in titles:
        print('-----------------')
        print(title)

        results = search_by_title(title, max_results=20)
        for result in results:
            dist = levenshtein_distance(title.lower(), result.title.lower())
            print(f"{dist}/{len(title)}: {result.title}")
            if dist < len(title) / 10:
                print('Match')
                data.append({
                    'reference': title,
                    'title': result.title,
                    'abstract': result.summary,
                    'url': result.entry_id
                })
                break
        else:
            print('No match! !!!!!')

    print(f'{len(data)}/{len(titles)} matches found')
    return data


def get_data():
    references = extract_references(file, last_page=-pages, sep=sep)
    abstracts = search_on_arxiv(references)

    with open(f'{file}.json', 'w') as f:
        json.dump(abstracts, f)


file = 'The_Impact_of_Large_Language_Modeling_on_Natural_Language_Processing_in_Legal_Texts_A_Comprehensive_Survey.pdf'
# file = 'The_Recent_Large_Language_Models_in_NLP.pdf'
# file = 'Multimodal_Large_Language_Models_A_Survey.pdf'
sep = '.'  # '“'
pages = 1  # 2

if __name__ == '__main__':
    get_data()
