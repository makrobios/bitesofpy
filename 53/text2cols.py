import re
from itertools import zip_longest

COL_WIDTH = 20

text = """My house is small but cosy.

It has a white kitchen and an empty fridge."""


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    output = ''
    WIDTH = COL_WIDTH - 2
    cols = text.split("\n\n")
    pat = re.compile(r"""\w                 # Pattern has to start with letter
                        [\w\s\.]{1,%d}      # At least one letter, whitespace up to WIDTH variable 
                        \w\b[\.!?,]?""" % WIDTH , re.VERBOSE)   # Pattern stops with letter, end of word and optional .!?,
    cols_width = [re.findall(pat, col) for col in cols]
    for line in zip(*cols_width):
        output += '\t'.join(line) + "\n"
    return output[:-1]