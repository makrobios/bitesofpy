from datetime import datetime, timedelta, date
import re

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    pat = re.compile(r"\d{4}-\d{2}-\d{2}")
    return set(date.fromisoformat(d) for d in re.findall(pat, data))


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    day = 1 
    while TODAY - timedelta(days=day) in dates:
        day += 1
    if not TODAY in dates:
        day -= 1
    return day