from collections import defaultdict, Counter
from pathlib import Path
from typing import List

from nltk.tokenize import regexp_tokenize

DATA_DIR_NAME = 'data'


def get_bigrams(corpus: List) -> List:
    return [(corpus[i], corpus[i + 1]) for i in range(len(corpus) - 1)]


def main():
    data_path = Path(DATA_DIR_NAME)
    file_name = data_path/input()
    with open(file_name, 'r', encoding='utf-8') as f:
        tokens = regexp_tokenize(f.read(), r'\S+')
    bigrams = get_bigrams(tokens)
    m_chain = defaultdict(Counter)
    for h, t in bigrams:
        m_chain[h].update([t])
    # print(f'Number of bigrams: {len(bigrams)}')
    m_chain = {k: v.most_common() for k, v in m_chain.items()}
    while True:
        idx = input()
        if idx == 'exit':
            break
        print(f'Head: {idx}')
        try:
            tails = m_chain[idx]
            for k, v in tails:
                print(f'Tail: {k}\tCount: {v}')
        except KeyError:
            print('Key Error. The requested word is not in the model. Please input another word.')
            continue


if __name__ == '__main__':
    main()
