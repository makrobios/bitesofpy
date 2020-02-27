STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10):
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""
    xmastree = """""" 
    width = rows 
    xmastree += f'{STAR: >{width}}\n'
    for row in range(1, rows + 1):
        width = row + rows - 1 
        leaves = (row * 2 - 1) * LEAF
        xmastree += f'{leaves: >{width}}\n'
    trunks = (rows + 1 if rows % 2 == 0 else rows) * TRUNK
    xmastree += f'{trunks: ^{rows * 2 - 1}}\n'
    xmastree += f'{trunks: ^{rows * 2 - 1}}\n'
    return xmastree
