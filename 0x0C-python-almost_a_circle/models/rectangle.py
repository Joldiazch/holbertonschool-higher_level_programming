#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    """  """

    def __init__(self, width, height, x=0, y=0, id=None):
        attributs = {'width': width, 'height': height, 'x': x, 'y': y}
        self.verificator(attributs)
        super().__init__(id=id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        at = {'width': value}
        self.verificator(at)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        at = {'height': value}
        self.verificator(at)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        at = {'x': value}
        self.verificator(at)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        at = {'y': value}
        self.verificator(at)
        self.__y = value

    def verificator(self, attributes):
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