#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid

    Args:
        grid ([List]): [List of List of integers]

    Returns:
        [int]: [Perimeter of the island]
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # This is a land cell
                # Check the cell above
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check the cell below
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check the cell to the left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check the cell to the right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
