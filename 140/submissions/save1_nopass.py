import sys
sys.path.append('..')
import os 
import pandas as pd
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/home/ch/programming/pybites/data/'

fname = 'summer.csv'
remote = os.path.join(BASE_URL, fname)
data = os.path.join(TMP, fname)
urlretrieve(remote, data)

def athletes_most_medals(data=data):
    rec = dict()
    df = pd.read_csv(data)
    women = df.query('Gender == "Women"').groupby(
            'Athlete')['Medal'].count().sort_values()
    men = df.query('Gender == "Men"').groupby(
            'Athlete')['Medal'].count().sort_values()
    best_man = list(men.iteritems())[-1]
    best_woman = list(women.iteritems())[-1]
    rec[best_man[0]] = best_man[1]
    rec[best_woman[0]] = best_woman[1]
    return rec

