#!/usr/bin/python3
""" Module that contains class Base """
import json
"""import csv """


class Base:
    """Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes data"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([cls.to_dictionary(obj)
                        for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            shape = cls(1, 1)
        elif cls.__name__ == "Square":
            shape = cls(1)
        shape.update(**dictionary)
        return shape

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        list_instances = []
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                string_json = f.read()
                temp = cls.from_json_string(string_json)
                for val in temp:
                    list_instances.append(cls.create(**val))
            return(list_instances)
        except BaseException:
            return(list_instances)
