from collections import namedtuple

from bs4 import BeautifulSoup
import requests

import re

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# url =  "https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html"
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)
    sel_soup = soup.select(".title, .controls")
    results = []
    for title, points in zip(*[iter(sel_soup)] * 2):
        tit = title.text.strip()
        string = points.span.text.strip()
        pnts = re.search(r'^\d+', string).group(0)
        comm = re.search(r'\| (\d+)', string).group(1)
        results.append(Entry(tit, int(pnts), int(comm)))           
    return sorted(results, key= lambda entry: -(entry.points + entry.comments))[:top]
    # you code