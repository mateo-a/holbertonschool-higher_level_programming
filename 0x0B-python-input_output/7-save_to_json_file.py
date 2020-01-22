#!/usr/bin/python3
import json
"""

Function that writes an Object to a text file, using a JSON representation

"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    Arguments:
        my_obj : a object
        filename (file): file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
