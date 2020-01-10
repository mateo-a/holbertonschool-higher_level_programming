#!/usr/bin/python3


class Square:
    """ Class Square that defines a square by: (based on 3-square.py) """

    def __init__(self, size=0):
        """Initializes the data"""
        self.size = size

    @property
    def size(self):
        """to retrieve size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """to set size"""
        if type(value) is not int:
            raise TypeError("size must be an number")
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """ Check if the squares have same area """
        return (self.area() == other.area())

    def __ne__(self, other):
        """ Check if the squares have different area """
        return (self.area() != other.area())

    def __gt__(self, other):
        """ Check if the square area is greater than other """
        return (self.area() > other.area())

    def __ge__(self, other):
        """ Check if the square area is greater or equal than other """
        return (self.area() >= other.area())

    def __lt__(self, other):
        """ Check if the square area is less than other """
        return (self.area() < other.area())

    def __le__(self, other):
        """ Check if the square area is less or equal than other """
        return (self.area() <= other.area())
