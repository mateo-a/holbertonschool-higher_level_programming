#!/usr/bin/python3
"""

Function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False.

"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise False.

    Arguments:
        obj: an object recived as parameter
        a_class: a class recived as parameter
    Return:
        True if the object is an instance of a class that inherited (directly
        or indirectly) from the specified class; otherwise False.
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
