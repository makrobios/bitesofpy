def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    factor = 2.54 if fmt == 'in' else 0.39370079
    try:
        fmt in ['cm', 'in']
    except:
        raise ValueError
        
    try:
        return value * factor
    except:
        raise TypeError
        