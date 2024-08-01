#!/usr/bin/python3
"""
Lockboxes module

This module contains the function canUnlockAll(boxes) that determines if all
the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists of integers representing the boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if len(boxes) == 0:
        return False
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    if len(keys) == len(boxes):
        return True
    return False
