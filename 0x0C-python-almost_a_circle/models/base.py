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
        file_name = cls.__name__ + ".json"
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        my_json = cls.to_json_string(list_dict)
        with open(file_name, mode="w") as f:
            f.write(my_json)

    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(10,10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode="r") as f:
                list_dict = cls.from_json_string(f.read())
            list_instances = []
            for dictionary in list_dict:
                list_instances.append(cls.create(dictionary))
            print(list_instances)
            return list_instances
        except:
            return []

        
