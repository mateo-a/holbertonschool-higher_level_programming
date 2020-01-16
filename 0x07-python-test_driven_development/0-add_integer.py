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
    if a != a:
        a = 89
    if b != b:
        b = 89
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
