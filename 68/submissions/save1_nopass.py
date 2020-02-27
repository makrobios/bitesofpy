def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return [char for char in input_string if char.isalnum()]