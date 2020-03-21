import re

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""

    matrix = [
            list(map(int,re.findall(r"\d+", line )))
            for line in grid.splitlines()
            if re.match(r"\d", line)
            ]
    start = len(matrix) // 2
    last_element = max(max(matrix)) + 1
    pos = [start, start]
    last_direction = "right"
    print(1, end=' ')

    for num in range(last_element):

        row, col = pos[0], pos[1] 
        # directions 
        directions = dict(up =    ([row - 1, col], UP),
                          right = ([row, col + 1], RIGHT),
                          down =  ([row + 1, col], DOWN),
                          left =  ([row, col - 1], LEFT))

        for direction, ((row, col), arrow) in directions.items():
            try:
                if matrix[row][col] == num:
                    if last_direction != direction:
                        print( arrow)
                    last_direction = direction
                    pos = [row, col]
                    print( num, end=' ')

            except IndexError:
                continue 


small_grid = """
21 - 22 - 23 - 24 - 25
 |
20    7 -  8 -  9 - 10
 |    |              |
19    6    1 -  2   11
 |    |         |    |
18    5 -  4 -  3   12
 |                   |
17 - 16 - 15 - 14 - 13
"""


print_sequence_route(small_grid)