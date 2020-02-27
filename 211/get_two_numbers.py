import random
from functools import wraps


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    # ... retry MAX_RETRIES times
    # ...
    # make sure you include this for testing:
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #
    @wraps(func)
    def wrapper(*args):
        try:
            func(*args)
            raise MaxRetriesException
        except ValueError:
            next
        except MaxRetriesException as exc:
            print(exc)
    return wrapper

@retry
def get_two_numbers(numbers):
    """Give a list of items pick 2 random ones,
       if both are not ints raise a ValueError
    """
    chosen = random.sample(numbers, 2)
    if not all(type(i) == int for i in chosen):
        raise ValueError('not all ints')

get_two_numbers(['a','b'])
