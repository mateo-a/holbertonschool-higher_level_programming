#!/usr/bin/python3
"""

Class BaseGeometry (based on 6-base_geometry.py)

"""


class BaseGeometry:
    """
    Class BaseGeometry (based on 6-base_geometry.py)
    """
    def area(self):
        """Raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
