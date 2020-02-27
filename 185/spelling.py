from difflib import SequenceMatcher
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, 'dictionary.txt')
if not os.path.isfile(DICTIONARY):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/dictionary.txt',
        DICTIONARY
    )


def load_words():
    'return dict of words in DICTIONARY'
    with open(DICTIONARY) as f:
        return {word.strip().lower() for word in f.readlines()}


def suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    if words is None:
        words = load_words()

    # you code
    max_ratio = (0, None)
    for word in words:
        cur_ratio = ((SequenceMatcher(None, misspelled_word, word).ratio()), word)
        if cur_ratio > max_ratio:
            max_ratio = cur_ratio
    return max_ratio[1]

