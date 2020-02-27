import re
def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    text = re.sub('\w+.*','',text)
    return sum([1 for char in text if char == ' '])