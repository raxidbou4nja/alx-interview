#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n: int) -> int:
    """
    script to calculate the minimum number of
    operations to reach 'n' characters.

    Args: (n) Integer, the target number of characters.

    Returns: Integer, the minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    current_length = 1
    while current_length < n:
        if n % current_length == 0:
            current_length *= 2
            operations += 2
        else:
            current_length += 1
            operations += 1

    return operations
