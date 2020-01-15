#!/usr/bin/python3
"""

Class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

"""


class Rectangle:
    """ Class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
    """
    def __init__(self, width=0, height=0):
        """Initializes the data"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """to retrieve width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """to set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To retrieve height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """To set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
