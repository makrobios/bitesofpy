from datetime import date, timedelta

def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    may = date(year,5,1)  
    sunday = 0
    for day in range(15):
        d = may + timedelta(days=day)
        sunday += 1 if d.weekday() == 6:
            if sunday == 1:
                return d
            sunday += 1

print(get_mothers_day_date(2014))