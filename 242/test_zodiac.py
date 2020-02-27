from datetime import datetime
import json
import os
from pathlib import Path
from urllib.request import urlretrieve

import pytest

from zodiac import (get_signs, get_sign_with_most_famous_people,
                    signs_are_mutually_compatible, get_sign_by_date)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope='module')
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)


def test_get_sign_with_most_famous_people(signs):
    assert get_sign_with_most_famous_people(signs) == ('Scorpio', 35)


    
params = [ ('Aries', 'Leo', True),
           ('Aries', 'Pisces', False),
           ('Gemini', 'Libra', True),
           ('Gemini', 'Scorpio', False) ]
@pytest.mark.parametrize('sign1, sign2, expected', params )
def test_signs_are_mutually_compatible(signs, sign1, sign2, expected):
    assert signs_are_mutually_compatible(signs, sign1, sign2) == expected 


    
params = [ ( datetime(2018,1,1), 'Capricorn'),
           ( datetime(2007,5,11), 'Taurus'),
           ( datetime(2001,3,24), 'Aries'),
           ( datetime(2007,8,1), 'Leo') ]
@pytest.mark.parametrize('date, expected', params)
def test_get_sign_by_date(signs, date, expected):
    assert get_sign_by_date(signs, date) == expected
    