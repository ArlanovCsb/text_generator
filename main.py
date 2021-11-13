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
    while True:
        head = random.choice(list(m_chain.keys()))
        if re.match('[A-Z]', head) and not re.search(r'\S+[.!?]$', head):
            break
    sentence = [head]
    sentence_cnt = 0
    while True:
        word = get_word_from_chain(m_chain[head])
        sen_end_word_search = re.search(r'\S+[.!?]$', word)
        if len(sentence) < MIN_NUM_WORDS and sen_end_word_search:
            continue
        sentence.append(word)
        if len(sentence) >= MIN_NUM_WORDS and sen_end_word_search:
            print(' '.join(sentence))
            sentence.clear()
            sentence_cnt += 1
            while True:
                head = get_word_from_chain(m_chain[word])
                if re.match('[A-Z]', head) and not re.search(r'\S+[.!?]$', head):
                    sentence.append(head)
                    break
        else:
            head = word
        if sentence_cnt == NUM_SENTENCES:
            return


if __name__ == '__main__':
    main()
