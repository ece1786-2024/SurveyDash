import argparse
import os
import json
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


def search_on_arxiv(titles):
    client = arxiv.Client()

    data = []

    for title in titles:
        print('-----------------')
        print(title)

        search = arxiv.Search(
            query="ti:" + title,
            max_results=20,
            sort_by=arxiv.SortCriterion.Relevance
        )

        results = client.results(search)

        for result in results:
            dist = levenshtein_distance(title.lower(), result.title.lower())
            print(f"{dist}/{len(title)}: {result.title}")
            if dist < len(title) / 10:
                print('Match')
                data.append({
                    'reference': title,
                    'title': result.title,
                    'authors': [a.name for a in result.authors],
                    'year': result.published.year,
                    'abstract': result.summary,
                    'url': result.entry_id
                })
                break
        else:
            print('No match! !!!!!')

    print(f'{len(data)}/{len(titles)} matches found')
    return data


def get_data(file_path):
    with open(file_path) as f:
        papers = f.read().split('\n')

    abstracts = search_on_arxiv(papers)

    directory = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    file_name = file_name.split('.')[0]
    with open(f'{directory}/../abs/{file_name}.json', 'w') as f:
        json.dump(abstracts, f, indent=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download references from a PDF file')
    parser.add_argument('file', type=str, help='Path to the PDF file')

    args = parser.parse_args()

    if os.path.isfile(args.file):
        get_data(args.file)
    elif os.path.isdir(args.file):
        for file in os.listdir(args.file):
            if file.endswith('.txt'):
                print(file)
                get_data(os.path.join(args.file, file))

"""
# Usage
python download_abs.py ./dataset/txt/1.txt
# OR
python download_abs.py ./dataset/txt/
"""
