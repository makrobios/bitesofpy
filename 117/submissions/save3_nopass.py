import math

def round_even(number):
    """Takes a number and returns it rounded even"""
    if math.remainder(number, int(number)) < 0.5 :
        return math.floor(number)
    else:
        return math.ceil(number)