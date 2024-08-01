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
    opened = [False] * n  # Keep track of opened boxes
    opened[0] = True  # The first box is already open
    keys = boxes[0]  # Start with the keys in the first box
    
    for key in keys:
        if key < n and not opened[key]:  # If the key is for a valid box and it's not yet opened
            opened[key] = True
            keys.extend(boxes[key])  # Add the keys from the newly opened box

    return all(opened)
