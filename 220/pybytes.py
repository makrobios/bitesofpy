from collections import namedtuple, Counter
import re
from typing import NamedTuple
from datetime import timedelta
import time

import feedparser

SPECIAL_GUEST = 'Special guest'

# using _ as min/max are builtins
Duration = namedtuple('Duration', 'avg max_ min_')

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = 'https://bites-data.s3.us-east-2.amazonaws.com/python_bytes'
IGNORE_DOMAINS = {'https://pythonbytes.fm', 'http://pythonbytes.fm',
                  'https://twitter.com', 'https://training.talkpython.fm',
                  'https://talkpython.fm', 'http://testandcode.com'}


class PythonBytes:

    def __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = feedparser.parse(url).entries

    def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        return [entry.itunes_episode 
                for entry in self.entries
                if domain in entry.summary] 

    def get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        counter = Counter()
        for entry in self.entries:
           counts = set((re.findall(r"https?://[^/]+", entry.summary)))
           counts = {domain for domain in counts if domain not in IGNORE_DOMAINS }
           counter.update(counts)
        return counter.most_common(n)
        
    def number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        return len([entry.itunes_episode
                for entry in self.entries
                if SPECIAL_GUEST in entry.summary])

    @staticmethod
    def _to_timedelta(time):
        h, m, s = map(int, time.split(":"))
        return timedelta(hours= h, minutes= m, seconds= s)

    @staticmethod
    def _duration():
        durations = []
        total = timedelta()
        count = 0
        while True:
            term = yield
            if term is None:
                break
            term = PythonBytes._to_timedelta(term)
            total += term
            durations += [term]
            count += 1
        _max = re.sub(r"^(\d:)",r"0\1", str(max(durations)))
        _min = re.sub(r"^(\d:)",r"0\1", str(min(durations))) 
        return Duration( (total/count).seconds,
                         _max,
                         _min) 

    def get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """
        gen = PythonBytes._duration()
        next(gen)
        for entry in self.entries:
            gen.send(entry.itunes_duration)
        try:
            gen.send(None)
        except StopIteration as exc:
            result = exc.value
        return result 
         