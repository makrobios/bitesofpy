from urllib.request import urlretrieve
import pandas as pd
from io import StringIO

TMP = '/tmp/table.csv'
XYZ = "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
THRESHOLDS = (5000, 0.05)
#r = urlretrieve(XYZ, TMP)
#text = open(TMP).read()

def calculate_flux(XYZ: str) -> list:
    """Read the data in from xyz.csv
    add two new columns, one to calculate dollar flux,
    and the other to calculate percentage flux
    return as a list of tuples
    """
    retrieve = urlretrieve(XYZ, '/tmp/table.csv')
    text = open('/tmp/table.csv').read()
    table = pd.read_csv( StringIO(text), index_col='Account' )    
    table['dollar_flux'] = table['12/31/20'] - table['12/31/19']
    table['percent_flux'] = table['dollar_flux'] / table['12/31/19']
    return list(table.itertuples())


def identify_flux(xyz: list) -> list:
    """Load the list of tuples, iterate through
    each item and determine if it is above both
    thresholds. if so, add to the list
    """
    flagged_lines = []
    for item in xyz:
        *orig, dol, perc = item
        if  abs(dol) > THRESHOLDS[0] and abs(perc) > THRESHOLDS[1]):
            flagged_lines.append(item)
    return flagged_lines