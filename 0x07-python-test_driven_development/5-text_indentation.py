#!/usr/bin/python3
"""

text_indentation: function that prints a text with 2 new lines after each of
                these characters: ., ? and :

"""


def text_indentation(text):
    """function that prints a text with 2 new lines after each
        of these characters: ., ? and :
    Args:
        text (str): the string text to print out
    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = "".join([char if char not in ".?:" else char + "\n\n"
                    for char in text])
    print("\n".join([x.strip() for x in line.split("\n")]), end="")
