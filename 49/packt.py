from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    parser = 'html.parser'
    soup = Soup(CONTENT, parser)  
    book = soup.find_all("div", {"class": "dotd-main-book cf"})[0]
    title = book.h2.text.strip()
    description = book.find('h2').parent.find_next_sibling().find_next_sibling().text.strip()
    link = book.a['href']
    image = book.img['src']
    return Book(title, description, image, link)

print(get_book())