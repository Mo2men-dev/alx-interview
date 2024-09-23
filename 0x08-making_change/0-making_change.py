#!/usr/bin/python3
"""
Making Change
"""


def fill_arr(amnt):
    """
    Function to pre-fill an array
    """

    arr = [amnt + 1 for x in range(amnt)]
    arr[0] = 0

    return arr


def makeChange(coins, total):
    """
    Function to solve make change problem
    """

    if total <= 0:
        return 0

    filled_arr = fill_arr(total)
    for curr_amnt in range(len(filled_arr)):
        for coin in coins:
            if coin > curr_amnt:
                break

            curr_min_change = filled_arr[curr_amnt - coin] + 1
            filled_arr[curr_amnt] = min(curr_min_change, filled_arr[curr_amnt])

    if filled_arr[-1] == total + 1:
        return -1

    return filled_arr[-1]
