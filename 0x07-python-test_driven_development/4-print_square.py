#!/usr/bin/python3
"""

print_square: function that prints a square with the character #

"""


def print_square(size):
    """function that prints a square with the character #
    Args:
        size (int): size length of the square
    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("#" * size)
