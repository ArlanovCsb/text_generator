from collections import defaultdict, Counter
from pathlib import Path
import random
import re
from typing import List, Dict

from nltk.tokenize import regexp_tokenize

DATA_DIR_NAME = 'data'
MIN_NUM_WORDS = 5
NUM_SENTENCES = 10


def get_bigrams(corpus: List) -> List:
    return [(corpus[i], corpus[i + 1]) for i in range(len(corpus) - 1)]


def get_trigrams(corpus: List) -> List:
    return [(f'{corpus[i]} {corpus[i + 1]}', corpus[i + 2]) for i in range(len(corpus) - 2)]


def get_markov_chain(ngrams: List) -> Dict:
    m_chain = defaultdict(Counter)
    for h, t in ngrams:
        m_chain[h].update([t])
    return {k: v.most_common() for k, v in m_chain.items()}


def get_word_from_chain(tails: List) -> str:
    return random.choices([x[0] for x in tails], [x[1] for x in tails])[0]


def get_start_head(heads: List) -> str:
    while True:
        head = random.choice(heads)
        if re.match('[A-Z]', head) and not re.search(r'\S+[.!?]$', head.split()[0]):
            break
    return head


def main():
    data_path = Path(DATA_DIR_NAME)
    file_name = data_path/input()
    with open(file_name, 'r', encoding='utf-8') as f:
        tokens = regexp_tokenize(f.read(), r'\S+')
    ngrams = get_trigrams(tokens)
    m_chain = get_markov_chain(ngrams)
    heads = list(m_chain.keys())
    head = get_start_head(heads)
    sentence = [*head.split()]
    sentence_cnt = 0
    while True:
        word = get_word_from_chain(m_chain[head])
        sentence.append(word)
        last_predicted_word = head.split()[1]
        if len(sentence) >= MIN_NUM_WORDS and re.search(r'\S+[.!?]$', word):
            print(' '.join(sentence))
            sentence.clear()
            sentence_cnt += 1
            head = get_start_head(heads)
            sentence.extend([*head.split()])
        else:
            head = f'{last_predicted_word} {word}'
        if sentence_cnt == NUM_SENTENCES:
            return


if __name__ == '__main__':
    main()
