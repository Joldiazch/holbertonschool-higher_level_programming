#!/usr/bin/python3

import json

class Base:
    """ first class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects += 1
        if id != None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None:
            my_json = cls.to_json_string(list_objs)
            with open("Rectangle.json", mode="w") as f:
               f.write(my_json)
