#!/usr/bin/python3
""" Module that contains class Base """
import json
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        filename = cls.__name__ + ".csv"
        objs = [cls.to_dictionary(obj) for obj in list_objs]
        try:
            with open(filename, mode="w", encoding="utf-8") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for obj in objs:
                    writer.writerow(obj)
        except BaseException:
            return "[]"

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        dic = []
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for obj in reader:
                    for key, value in obj.items():
                        obj[key] = int(value)
                    dic.append(obj)
            return [cls.create(**num_objs) for num_objs in dic]
        except BaseException:
            return dic

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares"""
        turtle.penup()
        turtle.pensize(10)
        turtle.bgcolor("black")
        turtle.color("cyan")
        turtle.hideturtle()
        turtle.goto(-300, 300)
        turtle.speed(0)

        for instance in list_rectangles:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 200
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 300)

        turtle.goto(-300, 100)
        for instance in list_squares:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 100
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 100)

        turtle.exitonclick()
