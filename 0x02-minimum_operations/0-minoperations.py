#!/usr/bin/python3

""" minOperations module """


def minOperations(n: int) -> int:
    """calculates the fewest number of operations (Copy All and Paste)
    needed to result in exactly n H characters.

    Args:
        n: integer

    Returns: number of operations (int), or 0 if n is impossible to achieve

    Example: n = 9 -> 6
    """

    if n == 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
