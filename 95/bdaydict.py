MSG = 'Hey {}, there are more people with your birthday!'

from datetime import date
class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        dates_existing = [(v.month, v.day) for v in self.values()]
        if (self.birthday.month, self.birthday.day) in dates_existing:
            print(MSG.format(self.name))
        self.update({self.name:self.birthday})

d = BirthdayDict()
d['a'] = date(2010,4,4)
d['b'] = date(2009,4,4)