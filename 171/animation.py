from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    start = time()
    for state in cycle(SPINNER_STATES):
        print(state, flush=True, end='\r')
        sleep(STATE_TRANSITION_TIME)
        if (time() - start) >= seconds:
            break


if __name__ == '__main__':
    spinner(2)