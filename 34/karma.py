from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:

    def __init__(self, name):
        self.name = name
        self._transactions = [] 
    
    def __add__(self, other):
        if isinstance(other, Transaction):
            self._transactions.append(other)
    def __str__(self):
        s = 's' if self.fans > 1 else '' 
        return f"{self.name} has a karma of {self.karma} and {self.fans} fan{s}"
    
    @property
    def points(self):
        return [t.points for t in self._transactions]

    @property
    def karma(self):
        return sum(self.points)
            
    @property
    def fans(self):
        self._fans = set(t.giver for t in self._transactions)
        return len(self._fans)
