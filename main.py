from nltk.tokenize import regexp_tokenize
from nltk.probability import FreqDist
from pathlib import Path

DATA_DIR_NAME = 'data'


def main():
    data_path = Path(DATA_DIR_NAME)
    file_name = data_path/input()
    with open(file_name, 'r', encoding='utf-8') as f:
        tokens = regexp_tokenize(f.read(), r'\S+')
    freq_dist = FreqDist(token for token in tokens)
    print('Corpus statistics')
    print(f'All tokens: {len(tokens)}')
    print(f'Unique tokens: {len(freq_dist)}')
    while True:
        idx = input()
        if idx == 'exit':
            break
        try:
            print(tokens[int(idx)])
        except ValueError:
            print('Type Error. Please input an integer.')
            continue
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
            continue


if __name__ == '__main__':
    main()
