#!/usr/bin/python3
""" import class base """
from models.base import Base


class Rectangle(Base):
    """ class Rectangule """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init class """
        attributs = {'width': width, 'height': height, 'x': x, 'y': y}
        self.verificator(attributs)
        super().__init__(id=id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width geter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        at = {'width': value}
        self.verificator(at)
        self.__width = value

    @property
    def height(self):
        """ height geter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        at = {'height': value}
        self.verificator(at)
        self.__height = value

    @property
    def x(self):
        """ x geter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        at = {'x': value}
        self.verificator(at)
        self.__x = value

    @property
    def y(self):
        """ y geter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        at = {'y': value}
        self.verificator(at)
        self.__y = value

    def verificator(self, attributes):
        """ verificator """
        msg1 = "{} must be an integer"
        msg2 = "{} must be > 0"
        msg3 = "{} must be >= 0"
        for att, value in attributes.items():
            if type(value) is not int:
                raise TypeError(msg1.format(att))
            if value <= 0 and att in ["width", "height"]:
                raise ValueError(msg2.format(att))
            if value < 0 and att in ["x", "y"]:
                raise ValueError(msg3.format(att))

    def area(self):
        """ area """
        return self.width * self.height

    def display(self):
        """ display """
        print("\n" * self.y, end="")
        x_position = " " * self.x
        row = x_position + ("#" * self.width)
        rows_less_last = (row + "\n") * (self.height - 1)
        print(rows_less_last + row)

    def __str__(self):
        """ str """
        msg1 = "[Rectangle] ({}) {}/{} - {}/{}"
        return msg1.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ update """
        if len(args) != 0:
            names = ["id", "width", "height", "x", "y"]
            idx = 0
            for value in args:
                setattr(self, names[idx], value)
                idx += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ to dictionary  """
        names = ["id", "width", "height", "x", "y"]
        dictionary = {}
        for name in names:
            dictionary[name] = getattr(self, name)
        return dictionary
