#!/usr/bin/python3
"""
Pascal's Triangle module

This module contains the function pascal_triangle(n) that returns a
list of lists of integers representing the Pascal’s triangle of n.

Example:
    pascal_triangle(5) -> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.

    Args:
        n (int): The number of rows of the Pascal's triangle to return.

    Returns:
        list: A list of lists of integers representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    if n == 1:
        return [[1]]
    
    output = [[1], [1, 1]]
    elements_to_add = 1

    for _ in range(2, n):
        nxt_arr = [1]
        for j in range(elements_to_add):
            nxt_el = output[elements_to_add][j] + output[elements_to_add][j + 1]
            nxt_arr.append(nxt_el)
        
        elements_to_add += 1
        nxt_arr.append(1)
        output.append(nxt_arr)
    
    return output
