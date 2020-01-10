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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)
