#!/bin/usr/python3
"""

Function that reads n lines of a text file (UTF8) and prints it to stdout

"""


def read_lines(filename="", nb_lines=0):
    """
    Function that reads n lines of a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for line in f:
                if nb_lines > 0:
                    print(line, end="")
                    nb_lines -= 1
                else:
                    break
