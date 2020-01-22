#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            if all(map(lambda x: True if type(x) is str else False, attrs)):
                my_dict = {}
                for attr in attrs:
                    try:
                        my_dict[attr] = getattr(self, attr)
                    except:
                        continue
                return my_dict
            else:
                return self.__dict__
        else:
            return self.__dict__
