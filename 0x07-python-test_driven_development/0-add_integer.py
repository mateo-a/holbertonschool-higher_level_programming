#!/usr/bin/python3
"""

add_integer: function that adds 2 integers

"""


def add_integer(a, b=98):
    """function that adds 2 integers
    Args:
        a (int): Number
        b (int): Number
    Returns:
        int: a + b casted to integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    if a != a:
        raise ValueError
    if b != b:
        raise ValueError

    result = a + b

    if result == float("inf") or result == -float("inf"):
        raise OverflowError

    return (result)
