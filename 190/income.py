import os
from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup
from collections import defaultdict

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    incomes = defaultdict(list)
    with open(xml, "r") as x:
        content = x.read()
        soup = BeautifulSoup(content, "lxml")
    levels = soup.find_all("wb:incomelevel")
    names = soup.find_all("wb:name")
    for name, level in zip(names, levels):
        incomes[level.text].append(name.text)
    return incomes
print(get_income_distribution())