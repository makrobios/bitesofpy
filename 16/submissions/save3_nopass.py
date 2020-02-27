from datetime import datetime
from datetime import timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)
hundred_days = timedelta(days=100)
birthdays = [ datetime(year=PYBITES_BORN.year + i,month=12, day=19) for i in (1,2,3,4)]

def gen_special_pybites_dates():
    new_date = PYBITES_BORN
    while True:
        if new_date < birthdays[0] < new_date + hundred_days:
            new_date +=  hundred_days
            yield birthdays.pop(0), new_date
        new_date += hundred_days
        yield new_date
        
#gen = gen_special_pybites_dates()
#l = []
#for i in range(10):
#    l.append(next(gen))
    
#print(l)