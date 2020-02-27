IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    filtered = []
    count = MAX_NAMES
    for name in names:
        contains_digit = any([str(char).isdigit() for char in name])
        ignore = name.startswith(IGNORE_CHAR) 
        if contains_digit or ignore:
            continue
        elif name.startswith(QUIT_CHAR) or count == 0:
            break
        else:
            count -= 1
            yield name