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
    types = [int, float]
    if type(a) not in types:
        raise TypeError("a must be an integer")
    if type(b) not in types:
        raise TypeError("b must be an integer")
    if type(a) is float('inf') or type(b) is float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if type(a) is float('NaN') or type(b) is float('NaN'):
        raise OverflowError("cannot convert float NaN to integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
