# Pybites Bite 145 https://codechalleng.es/bites/145/

import os
from collections import namedtuple, defaultdict
from datetime import date
from urllib.request import urlretrieve
import operator

import pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/"
STATION = namedtuple("Station", "ID Date Value")

fname = 'weather-ann-arbor.csv'
DIR = '/tmp'
local = os.path.join(DIR, fname)
remote = os.path.join(DATA_FILE, fname)

urlretrieve(remote, local) 

def high_low_temps():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value
         
    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    #modify Dataframe and correct Data_Values
    df = pd.read_csv(local, parse_dates=['Date'])
    df.set_index('Date', inplace = True)
    df['Data_Value'] = df['Data_Value'] / 10

    past = df.loc['2005':'2014']
    now = df.loc['2015']

    records = []
    days = defaultdict(lambda: defaultdict(list))
    # save entries from 2005-2014 in defaultdictionary 
    # dict[Month-Day][TMIN/TMAX] = [List of Values]
    for entry in past.itertuples():
        month = entry.Index.month
        day = entry.Index.day
        value = entry.Data_Value
        elem = entry.Element
        date = f'{month}-{day}'
        days[date][elem].append(value)
    
    for item in now.itertuples():
        month = item.Index.month
        day = item.Index.day
        date = f'{month}-{day}'
        op = operator.gt
        func = max
        elem = item.Element
        if elem == 'TMIN':
            op = operator.lt
            func = min
        if op( item.Data_Value, func(days[date][elem]) ):
            records.append(item) 
    high = max( records, key=lambda x: x.Data_Value )
    low  = min( records, key=lambda x: x.Data_Value )
    high = STATION(high.ID, high.Index.date(), high.Data_Value)
    low = STATION( low.ID, low.Index.date(), low.Data_Value )
    return ( high, low )