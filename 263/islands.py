def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continously
        connected vertically or horizontically  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    # islands = 0         # var. for the counts
    # .....some operations.....
    # mark_islands(r, c, grid)
    # return islands
    islands =0
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if grid[i][j] == 1:
                mark_islands(i, j, grid)
                extend_island(i, j, grid)
                islands += 1
    return islands

def extend_island(row, col, grid):
    """
    extends island
    try to find 1 in four directions recursively
    and marks islands:
    """
    up = (row - 1, col)
    right = (row, col + 1)
    down = (row + 1, col)
    left = (row, col -1)
    for (row, col) in [down, right, up, left]:
        if row < 0 or col < 0:
            continue
        try:
            if grid[row][col] == 1:
                mark_islands(row, col, grid)
                extend_island(row, col, grid)
        except IndexError:
            print(f"No Value found in {row}, {col}")


def mark_islands(row, col, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visisted islands as in-place operation.
    """
    # grid[i][j] = '#'      # one way to mark visited ones - suggestion.
    grid[row][col] = '#'
