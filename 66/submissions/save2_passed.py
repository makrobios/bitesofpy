from itertools import accumulate
import statistics
def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    for idx, acc in enumerate(accumulate(sequence), 1):
        yield round(acc/idx,2)