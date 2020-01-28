#!/usr/bin/python3
""" for work with json files"""
import json
import turtle


class Base:
    """ first class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init class """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json to string  """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        file_name = cls.__name__ + ".json"
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        my_json = cls.to_json_string(list_dict)
        with open(file_name, mode="w") as f:
            f.write(my_json)

    @staticmethod
    def from_json_string(json_string):
        """ from json string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create """
        if cls.__name__ is "Rectangle":
            dummy = cls(10, 10)
        else:
            dummy = cls(10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load from file """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode="r") as f:
                read = f.read()
                list_dict = cls.from_json_string(read)
            list_instances = []
            for dictionary in list_dict:
                obj = cls.create(**dictionary)
                list_instances.append(obj)
            return list_instances
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to file """
        file_name = cls.__name__ + ".csv"
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        my_json = cls.to_json_string(list_dict)
        with open(file_name, mode="w") as f:
            f.write(my_json)

    @classmethod
    def load_from_file_csv(cls):
        """ load from file """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, mode="r") as f:
                read = f.read()
                list_dict = cls.from_json_string(read)
            list_instances = []
            for dictionary in list_dict:
                obj = cls.create(**dictionary)
                list_instances.append(obj)
            return list_instances
        except:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        t = turtle.Turtle()
        for rect in list_rectangles:
            t.hideturtle()
            t.penup()
            t.goto(rect.x, rect.y)
            t.showturtle()
            t.pendown()
            for l in [rect.width, rect.height, rect.width, rect.height]:
                t.forward(l)
                t.left(90)

        for squ in list_squares:
            t.hideturtle()
            t.penup()
            t.goto(squ.x, squ.y)
            t.showturtle()
            t.pendown()
            for l in range(4):
                t.forward(squ.size)
                t.left(90)
        t.done()
