from datetime import datetime
import pytz
from functools import partial

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)
utc =  datetime(2018, 4, 18, 13, 28)
timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']

def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    if not all(tz in TIMEZONES for tz in timezones):
        raise ValueError
    utc = pytz.timezone('UTC').localize(utc)
    if all( utc.astimezone(pytz.timezone(time)).hour 
            in MEETING_HOURS 
            for time in timezones ):
        return True
    else:
        return False
