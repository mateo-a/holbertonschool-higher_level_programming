#!/usr/bin/python3
import json
"""

Function that creates an Object from a “JSON file”

"""


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”
    Arguments:
        filename (file): file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return(json.load(f))
