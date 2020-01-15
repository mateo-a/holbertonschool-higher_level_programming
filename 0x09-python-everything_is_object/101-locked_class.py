#!/usr/bin/python3
"""

Prevents the user from dynamically creating new instance attributes

"""


class LockedClass:
    """Class without class or object attribute"""
    __slots__ = "first_name"
