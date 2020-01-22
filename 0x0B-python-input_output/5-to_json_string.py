#!/usr/bin/python3
"""

Function that returns the JSON representation of an object (string)

"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)
    Arguments:
        my_obj : a object
    Returns:
        The JSON representation
    """
    return json.dumps(my_obj)
