import random
from collections import namedtuple
from itertools import combinations

Indexed = namedtuple('Indexed', 'idx val')
lst = random.sample(range(1,11),10)

def _combinations(sorted_indexed, target):
    combi = combinations(sorted_indexed, 2) 
    for lo, hi in combi:
        if lo.val + hi.val == target:
            return lo.idx, hi.idx

def two_sums(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    indexed = []
    for idx, num in enumerate(numbers):
        indexed.append(Indexed(idx, num))
    sorted_indexed = sorted(indexed, key=lambda tup: tup.val)
    return _combinations(sorted_indexed, target)