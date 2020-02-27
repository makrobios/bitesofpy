#Pybites Bite 3 https://codechalleng.es/bites/3/
import os
import urllib.request

# PREWORK
#TMP = os.getenv("TMP", "/tmp")
DIR = '/home/ch/programming/pybites/data'
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(DIR, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    words = []
    with open(DICTIONARY) as d:
        for line in d:
            words.append(line.strip())
        return words 

def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    value = 0
    for char in word.upper():
        try:
            value += LETTER_SCORES[char]
        except KeyError:
            continue
    return value

def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    wordlist = []
    for word in words:
        wordlist.append(( word, calc_word_value(word) ))
    maximum = max(wordlist, key=lambda x: x[1])
    return maximum[0]

print(max_word_value(load_words()))

