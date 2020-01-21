#!/usr/bin/python3
"""

Function that returns True if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class;
otherwise False

"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class;
    otherwise False

    Arguments:
        obj: an object recived as parameter
        a_class: a class recived as parameter
    Return:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class ; otherwise False.
    """
    return(isinstance(obj, a_class))
