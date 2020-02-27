import os
import urllib.request

import re
from collections import defaultdict
TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


def create_chart():
    safari = defaultdict(list)
    keywords = 'sending to slack channel'
    PYTHONMARKER = 0
    with open(SAFARI_LOGS) as sfile:
        for line in sfile:
            if 'python' in line.lower():
                PYTHONMARKER = 1
            elif '- cached, skipping' in line:
                PYTHONMARKER = 0
            elif keywords in line:
                date = re.match(r'\d\d-\d\d', line).group(0)
                symbol = PY_BOOK if PYTHONMARKER else OTHER_BOOK
                safari[date].append(symbol) 
                PYTHONMARKER = 0
    for day, books in safari.items():
        print(f"{day} {''.join(books)}")
