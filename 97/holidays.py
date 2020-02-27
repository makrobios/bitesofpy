from datetime import datetime
from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)

def _date(datestring): 
    return datetime.strptime(datestring, "%Y-%m-%d") 

def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    holidays = defaultdict(list)
    parser = "html.parser"
    soup = BeautifulSoup(content, parser)
    table = soup.find("table",{"class":"list-table"})
    rows = table.find_all('tr')

    for row in rows[1:]:
        month = _date(row.find('time').text).month
        month = f'{month:02d}'
        holiday = row.find('a').text
        holidays[month].append(holiday)
    return holidays
print(get_us_bank_holidays())