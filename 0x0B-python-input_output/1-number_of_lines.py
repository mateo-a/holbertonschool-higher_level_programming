#!/bin/usr/python3
"""

Function that returns the number of lines of a text file

"""


def number_of_lines(filename=""):
    """
    Function that returns the number of lines of a text file
    """
    line_number = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line_number += 1
    return(line_number)
