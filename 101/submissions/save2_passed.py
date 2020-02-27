MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    no = ''
    if age < 18:
        no = ' not'
    print(f'{name} is{no} allowed to drive')