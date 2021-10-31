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
    print(f'Number of bigrams: {len(bigrams)}')
    while True:
        idx = input()
        if idx == 'exit':
            break
        try:
            print(f'Head: {bigrams[int(idx)][0]}\tTail: {bigrams[int(idx)][1]}')
        except ValueError:
            print('Type Error. Please input an integer.')
            continue
        except IndexError:
            print('Index Error. Please input a value that is not greater than the number of all bigrams.')
            continue


if __name__ == '__main__':
    main()
