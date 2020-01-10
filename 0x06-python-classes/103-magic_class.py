#!/usr/bin/python3
import math


class MagicClass:
    """Class Magic Circle"""
    def __init__(self, radius=0):
        """Initializes the data"""
        self.__radius = 0
        if (type(radius) is not int) and (type(radius) is not float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the circle area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Returns the circle perimeter"""
        return (2 * math.pi * self.__radius)
