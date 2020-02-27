from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    notify = start_date
    while True:
        notify += timedelta(days=num_days)
        for i in range(num_bites):
            yield notify