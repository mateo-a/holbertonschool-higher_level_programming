#!/usr/bin/python3
"""
    Function that adds two numbers together
"""


def add_integer(a, b=98):
    """adds two numbers
    Args:
       a: integer or float
       b: integer or float, defalt to 98
    Returns:
       values added
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
