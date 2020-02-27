from itertools import tee
import pysnooper


scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


def _pairwise(iterable):
    a, b = tee(iterable)
    next(b,None)
    return zip(a,b)
#@pysnooper.snoop(watch="_get_belt")
class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        for rng, rank in zip(scores[1:], ranks):
            if new_score in range(rng):
                new_belt = rank.title()
                if self._last_earned_belt != new_belt:
                    self._last_earned_belt = new_belt
                    return (
                           f'Congrats, you earned {new_score} points '
                           f'obtaining the PyBites Ninja {new_belt} Belt')
                else:
                    return (f"Set new score to {new_score}")

    def _get_score(self):
        return self._score 

    def _set_score(self, new_score):
        if not isinstance(new_score, int):
            raise ValueError("Please supply an integer")
        elif new_score < self._score:
            raise ValueError(f"New Score must be larger than {self._score}")
        else:
            self._score = new_score 
            print(self._get_belt( new_score ),end="")
    score = property(_get_score, _set_score)