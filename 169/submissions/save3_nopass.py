def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    factor = 2.54 if fmt == 'cm' else 0.39370079
    
    if fmt.lower() not in ['cm', 'in']:
        raise ValueError
    try:
        return round(value * factor, 4)
    except:
        raise TypeError
        