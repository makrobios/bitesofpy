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
    islands = 0
    for row_num, row in enumerate(grid):
        for col_num, space in enumerate(row):
            if row_num == 0:
                grid, icount = mark_islands(row_num, col_num, grid)
                islands += icount
            else:
                grid, icount = mark_islands(row_num, col_num, grid)
                islands += icount
    return grid, islands
def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visisted islands as in-place operation.
    """
    # grid[i][j] = '#'      # one way to mark visited ones - suggestion.
    element = grid[i][j]
    if element == 1:
        if j == 0 or grid[i][j-1] == 0:
            grid[i][j] = '-'
            return (grid, 1)
        elif grid[i][j-1] == '-':
            grid[i][j] = '-'
            return (grid, 0)
    else:
        return (grid, 0)
        
grid = [[1, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 1]] 
print(count_islands(grid))