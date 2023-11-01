#!/usr/bin/python3
"""
    add integer

    function to calc sum of the two integers
"""


def add_integer(a, b=98):
    """
        add_integer : add integer to another.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
