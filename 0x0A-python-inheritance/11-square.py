#!/usr/bin/python3
"""

Class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle (9-rectangle.py).
    (task based on 10-square.py).
    """
    def __init__(self, size):
        """
        Instantiation with size
        Arguments:
            size (int): value for size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """makes nice string"""
        return("[{}] {s}/{s}".format(self.__class__.__name__, s=self.__size))
