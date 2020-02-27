# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    media = dict()
    for platforms in social_platforms.strip().split("\n\n"):
        name, rng_min, rng_max, regex = platforms.split("\n")
        name = name.strip()
        rng_min = int(rng_min.split(":")[1].strip())
        rng_max = int(rng_max.split(":")[1].strip())
        pat = regex.split(":")[1]
        regex = re.compile(rf"[{pat}]*")
        media[name] = Validator(range(rng_min, rng_max), regex) 
    return media


def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    if platform not in all_validators:
        raise ValueError
    validator = all_validators[platform]
    if re.fullmatch(validator.regex, username) and len(username) in validator.range:
        return True
    else:
        return False

