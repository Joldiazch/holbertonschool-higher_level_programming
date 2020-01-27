#!/usr/bin/python3
""" Rectagle class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ init method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str method """
        msg = "[Square] ({}) {}/{} - {}"
        return msg.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ size property """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update """
        if len(args) != 0:
            names = ["id", "width", "x", "y"]
            idx = 0
            for value in args:
                setattr(self, names[idx], value)
                idx += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ to dictionary """
        names = ["id", "size", "x", "y"]
        dictionary = {}
        for name in names:
            dictionary[name] = getattr(self, name)
        return dictionary
