#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes data"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string of square"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    @property
    def size(self):
        """Get size"""
        return self.width

    @size.setter
    def size(self, size):
        """Set size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return({"id": self.id, "size": self.size,
                "x": self.x, "y": self.y})
