#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        msg = "[Square] ({}) {}/{} - {}"
        return msg.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
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
        names = ["id", "size", "x", "y"]
        dictionary = {}
        for name in names:
            dictionary[name] = getattr(self, name)
        return dictionary