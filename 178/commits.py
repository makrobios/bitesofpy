from collections import Counter, defaultdict
import os
from urllib.request import urlretrieve
from dateutil.parser import parse

import re
commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    with open(commit_log) as com:
        commitstable = defaultdict(int)    
        for line in com.readlines():
            date, changes = line.replace("Date:   ","").split('|')
            pdate = parse(date).strftime("%Y-%m")
            pchanges = re.findall(r'\d+', changes)[1:]  # skip changes in files
            commitstable[pdate] += sum(int(p) for p in pchanges)
        if year:
            commitstable = {key: value 
                           for key, value in commitstable.items() 
                           if key.split('-')[0] == str(year)} 
        return ( min(commitstable.items(), key= lambda tup: tup[1])[0],
                 max(commitstable.items(), key= lambda tup: tup[1])[0] )
