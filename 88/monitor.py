from collections import Counter
from contextlib import contextmanager
from datetime import date
from time import time, sleep


OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = Counter()


def get_today():
    """Making it easier to test/mock"""
    return date.today()


@contextmanager
def timeit():
    starttime = time() 
    yield # everything after yield will be executed as __exit__
    duration = time() - starttime
    if duration > OPERATION_THRESHOLD_IN_SECONDS:
        violations.update([get_today()])
        if any(val for key, val in violations.items() if val >= ALERT_THRESHOLD):
            print(ALERT_MSG)

