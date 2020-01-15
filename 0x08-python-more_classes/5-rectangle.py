#!/usr/bin/python3
"""

Class Rectangle that defines a rectangle by: (based on 4-rectangle.py)

"""


class Rectangle:
    """ Class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
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

    def area(self):
        """ Returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ Returns the rectangle perimeter"""
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """Print the rectangle with the character #"""
        if (self.__width == 0) or (self.__height == 0):
            return ("")
        return ("\n".join(["#" * self.__width for i in range(self.__height)]))

    def __repr__(self):
        """return a string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Print message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
