#!/usr/bin/python3
"""

Class Student that defines a student

"""


class Student:
    """Class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the data
        Args:
            first_name (str): firstname
            last_name (str): lastname
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance
        (same as 10-class_to_json.py)"""
        return(self.__dict__)
