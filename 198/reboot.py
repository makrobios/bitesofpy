import re
from dateutil.parser import parse
from itertools import tee

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""

def _pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a,b)

def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    result = []
    pat = re.compile(r"reboot\s+~\s+")
    sub = re.sub(pat,"", reboots)
    parse_dates = [ parse(line) for line in sub.splitlines()[:0:-1] ]
    pairwise = _pairwise(parse_dates)
    for cur, nxt in pairwise:
        days = (nxt - cur).days
        result.append( (days, nxt.strftime("%Y-%m-%d") ) )
    return max(result)
