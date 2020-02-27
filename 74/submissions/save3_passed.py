import calendar


def weekday_of_birth_date(date):
    year, month, day = date.year, date.month, date.day
    """Takes a date object and returns the corresponding weekday string"""
    tag = calendar.weekday(year=year, month=month, day=day)
    return calendar.day_name[tag]