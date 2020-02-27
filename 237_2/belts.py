import json
from pathlib import Path
from datetime import date, datetime as dt

SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
BELTS = ('white yellow orange green blue brown black '
         'paneled red').split()
TMP = Path('/tmp')

def get_belts(data: str) -> dict:
    """Parsed the passed in json data:
       {"date":"5/1/2019","score":1},
       {"date":"9/13/2018","score":3},
       {"date":"10/25/2019","score":1},

       Loop through the scores in chronological order,
       determining when belts were achieved (use SCORES
       and BELTS).

       Return a dict with keys = belts, and values =
       readable dates, example entry:
       'yellow': 'January 25, 2018'
    """
    ranges = list(zip(SCORES, BELTS))
    dates = dict()
    running = 0

    with open(data) as dat:
        jsdat = json.load(dat)

    for d in jsdat:
        d.update((k, dt.strptime(v,"%m/%d/%Y")) for k, v in d.items() if k == 'date')

    jsdat.sort(key=lambda x: x['date'])

    for entry in jsdat:
        running += entry['score']
        if running >= ranges[0][0]:
            _, grade = ranges.pop(0)
            date = entry['date']
            dates[grade] = date.strftime("%B %d, %Y") 
        if running > 1000:
            break
    return dates