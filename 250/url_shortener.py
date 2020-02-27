from math import floor
from string import ascii_letters, digits
from typing import Dict
from itertools import cycle

CODEX: str = digits + ascii_letters
BASE: int = len(CODEX)
# makeshift database record
LINKS: Dict[int, str] = {
    1: "https://pybit.es",
    45: "https://pybit.es/pages/articles.html",
    255: "http://pbreadinglist.herokuapp.com",
    600: "https://pybit.es/pages/challenges.html",
    874: "https://stackoverflow.com",
}
SITE: str = "https://pybit.es"

# error messages
INVALID = "Not a valid PyBites shortened url"
NO_RECORD = "Not a valid shortened url"

_encode_table = { num: bytes(letter, 'ascii') for (num, letter) in enumerate(CODEX) }

def encode(record: int) -> str:
    """Encodes an integer into Base62"""
    remain = record % BASE 
    result = CODEX[remain]
    queue = record // 62
    while queue:
        remain = queue % BASE
        queue = queue // BASE
        result = CODEX[remain] + result
    return result

def decode(short_url: str) -> int:
    """Decodes the Base62 string into a Base10 integer"""
    value = 0
    for char in short_url :
        value = BASE * value + CODEX.find(char)
    return value


def redirect(url: str) -> str:
    """Retrieves URL from shortened DB (LINKS)

    1. Check for valid domain
    2. Check if record exists
    3. Return URL stored in LINKS or proper message
    """
    breakpoint()
    if not SITE in url:
        return INVALID
    short = url.replace(SITE + "/", "")
    link = int(decode(short))
    if link in LINKS:
        return LINKS[link]
    else:
        return NO_RECORD

def shorten_url(url: str, next_record: int) -> str:
    """Shortens URL and updates the LINKS DB

    1. Encode next_record
    2. Adds url to LINKS
    3. Return shortened URL
    """
    short = encode(next_record)
    short_url = f"{SITE}/{short}"
    LINKS[next_record] = url 
    return short_url