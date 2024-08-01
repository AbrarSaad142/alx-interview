#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = boxes[0]

    for key in keys:
        if key < n and not opened[key]:
            opened[key] = True
            keys.extend(boxes[key])

    return all(opened)
