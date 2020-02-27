from collections import namedtuple, Counter
import re
from typing import NamedTuple

import feedparser

SPECIAL_GUEST = 'Special guest'

# using _ as min/max are builtins
Duration = namedtuple('Duration', 'avg max_ min_')

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = 'https://bites-data.s3.us-east-2.amazonaws.com/python_bytes'
IGNORE_DOMAINS = {'https://pythonbytes.fm', 'http://pythonbytes.fm',
                  'https://twitter.com', 'https://training.talkpython.fm',
                  'https://talkpython.fm', 'http://testandcode.com'}


def tstamp_str_to_seconds(tstamp):
    hh, mm, ss = tstamp.split(':')
    return int(hh)*60*60 + int(mm)*60 + int(ss)


class PythonBytes:

    def __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = feedparser.parse(url)['entries']

    def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        return [entry.itunes_episode for entry in
                self.entries if domain in entry.description]

    def get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        urls = Counter()
        for entry in self.entries:
            for url in set(re.findall(r'(https?://[^/]+)', entry.description)):
                if url in IGNORE_DOMAINS:
                    continue
                urls[url] += 1
        return urls.most_common(n)

    def number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        return len(
            [entry for entry in self.entries
             if SPECIAL_GUEST in entry.description]
        )

    def get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """
        durations = {
            tstamp_str_to_seconds(entry.itunes_duration): entry.itunes_duration
            for entry in self.entries
        }
        max_, min_ = max(durations), min(durations)
        avg = int(sum(durations) / len(durations))
        return Duration(avg=avg,
                        max_=durations[max_],
                        min_=durations[min_])
