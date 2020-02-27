def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    STAR = '*'
    SPACE = ' '
    xmastree = ''
    for stars, row in enumerate(range(rows,0,-1),1):
        multi = row - 1
        xmastree += f'{SPACE * {row -1} + STAR * (stars * 2 - 1)}\n'
    return xmastree.rstrip('\n')
