#!/usr/bin/python3
"""

Class Student that defines a student by: (based on 11-student.py)

"""


class Student:
    """Class Student that defines a student by: (based on 11-student.py)"""

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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        (same as 10-class_to_json.py)
        Args:
            attrs (str): a list of strings
        """
        if attrs is None:
            return self.__dict__
        new = {}
        for attrib in attrs:
            if attrib in self.__dict__:
                new[attrib] = self.__dict__[attrib]
        return(new)

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        Args:
            json (dict): dictionary
        """
        if not json:
            return
        self.__dict__ = json
