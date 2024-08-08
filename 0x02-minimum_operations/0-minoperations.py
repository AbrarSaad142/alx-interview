#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n):
    """Copy/Paste"""
    if n <= 1:
        return 0

    operation_needed = 0
    clipbord = 0
    current_lenght = 1

    while current_lenght < n:
        # If n is divisible by current length, we can copy all
        if n % current_lenght == 0:
            # This is the only time we can copy
            clipbord = current_lenght
            operation_needed += 1

        current_lenght += clipbord
        operation_needed += 1

    return operation_needed
