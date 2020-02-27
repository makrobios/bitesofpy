import csv

import requests
from collections import defaultdict
CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    req = requests.get(CSV_URL)
    return req.text

def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    result = defaultdict(int)
    reader = csv.DictReader(content.splitlines())
    for line in reader:
       result[line['tz']] += 1
    
    result_sorted = sorted(result.items(), key = lambda x: x[0])

    for key, value in result_sorted:
        print(f'{key:<20} | {"+" * value}')


