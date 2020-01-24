#!/usr/bin/python3


class Base:
    """ first class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects += 1
        if id != None:
            self.id = id
        else:
            self.id = Base.__nb_objects
