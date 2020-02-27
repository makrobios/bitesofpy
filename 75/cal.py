WEEKDAYS = "Su Mo Tu We Th Fr Sa".split()

def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    weeks = []

    for line in calendar_output.splitlines()[2:]:
        days = line.split()
        weeks.append(days)

    first_offset = 7 - len(weeks[0])
    last_offset = 7 - len(weeks[-1])
    weeks[0] = first_offset * [' '] + weeks[0]
    weeks[-1] = weeks[-1] + last_offset * [' '] 
    weekdays = dict() 
    for week in weeks:
        weekdays.update({int(day):wday for day, wday in zip(week, WEEKDAYS) if day.strip()}) 
    return weekdays


