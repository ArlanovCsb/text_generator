from collections import defaultdict, Counter
from pathlib import Path
import random
from typing import List, Dict

from nltk.tokenize import regexp_tokenize

DATA_DIR_NAME = 'data'
NUM_WORDS = 10
NUM_SENTENCES = 10
RANDOM_SEED = 23
random.seed(RANDOM_SEED)


def get_bigrams(corpus: List) -> List:
    return [(corpus[i], corpus[i + 1]) for i in range(len(corpus) - 1)]


def get_markov_chain(bigrams: List) -> Dict:
    m_chain = defaultdict(Counter)
    for h, t in bigrams:
        m_chain[h].update([t])
    return {k: v.most_common() for k, v in m_chain.items()}


def get_word_from_chain(tails: List) -> str:
    return random.choices([x[0] for x in tails], [x[1] for x in tails])[0]


def main():
    data_path = Path(DATA_DIR_NAME)
    file_name = data_path/input()
    with open(file_name, 'r', encoding='utf-8') as f:
        tokens = regexp_tokenize(f.read(), r'\S+')
    bigrams = get_bigrams(tokens)
    m_chain = get_markov_chain(bigrams)
    head = random.choice(list(m_chain.keys()))
    sentence = [head]
    for _ in range(NUM_WORDS * NUM_SENTENCES - 1):
        word = get_word_from_chain(m_chain[head])
        sentence.append(word)
        head = word
        if len(sentence) == 10:
            print(' '.join(sentence))
            sentence.clear()


if __name__ == '__main__':
    main()
