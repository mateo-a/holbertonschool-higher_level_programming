#!/usr/bin/python3


class Square:
    """ Class Square that defines a square by: (based on 3-square.py) """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ To retrieve position """
        return self.__position

    @position.setter
    def position(self, value):
        """ To set position """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.position[0] + "#" * self.__size
                            for i in range(self.__size)]))
