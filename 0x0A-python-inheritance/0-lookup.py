#!/usr/bin/python3
"""

Function that returns the list of available attributes and methods of an object

"""


def lookup(obj):
    """
    Function that retursn the list of available attributes and methods of an
    object

    Arguments:
        obj: an object recived as parameter
    Return:
        A list object
    """
    return (dir(obj))
