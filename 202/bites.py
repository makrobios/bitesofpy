import csv
import os
from pathlib import Path
from urllib.request import urlretrieve
from operator import itemgetter

import re

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    bites = []
    with open(stats, "r", encoding='utf-8-sig') as sta:
        for bite in csv.DictReader( sta.read().splitlines(), delimiter=";" ):
            try:
                number = re.search(r"^Bite (\d+)\.", bite["Bite"]).group(1)
            except AttributeError:
                continue 
            difficulty = float(bite['Difficulty']) if bite['Difficulty'] != "None" else 0 
            bites.append( ( number, difficulty ) )
    return [ num[0] for num in sorted(bites, key=itemgetter(1),reverse=True)[:N] ]

if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)