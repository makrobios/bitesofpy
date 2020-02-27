from string import ascii_lowercase
#import pysnooper

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ALPHABET = list(ascii_lowercase)

#@pysnooper.snoop()
def binary_search(sequence, target):
    pick = len(sequence) // 2

    if len(sequence) == 1 and sequence[pick] != target:
        raise TypeError
            
    elif sequence[pick] == target:
        return pick

    elif sequence[pick] > target:
        try:
            return binary_search(sequence[:pick], target)
        except TypeError:
            return None

    elif sequence[pick] < target:
        try:
            return pick + binary_search(sequence[pick:], target)
        except TypeError:
            return None