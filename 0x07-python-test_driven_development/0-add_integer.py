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
    if isinstance(a, (int, float)):
        a = int(a)
        if isinstance(b, (int, float)):
            b = int(b)
            return int(a + b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
