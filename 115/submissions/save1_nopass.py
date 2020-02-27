def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    return sum([1 for char in text.rstrip() if char == ' '])