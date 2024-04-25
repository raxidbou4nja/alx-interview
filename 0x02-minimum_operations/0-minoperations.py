#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n: int) -> int:
    """
    script to calculate the minimum number of
    operations to reach 'n' characters.

    Args: (n) Integer, the target number of characters.

    Returns: Integer, the minimum number of operations required.
    """
    next = 'H'
    body = 'H'
    operation = 0
    while (len(body) < n):
        if n % len(body) == 0:
            operation += 2
            next = body
            body += body
        else:
            operation += 1
            body += next
    if len(body) != n:
        return 0
    return operation
