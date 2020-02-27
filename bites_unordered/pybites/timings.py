from pathlib import Path
from urllib.request import urlretrieve

import re
tmp = Path('/tmp')
timings_log = tmp / 'pytest_timings.out'
if not timings_log.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )
def input():
    with open(timings_log) as time:
        return time.readlines()
    
timings = input() 

def get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    times = dict()
    skip_parse = ['error', 'no']
    for line in timings:
        if not any(w in line for w in skip_parse):
            bite, passed, seconds = re.findall(r'^(\d+) \=+ (\d+) passed(?:, \d+ warnings)? in (\d+\.\d+) seconds', line)[0]
            avg = int(passed)/float(seconds)
            times[bite] = avg
    return  max(zip(times.values(), times.keys()))[1] 
            
