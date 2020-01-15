#!/usr/bin/python3
"""class Rectangle that defines a Rectangle"""


class Rectangle:
    """class Rectangle that defines a Rectangle"""
    def __init__(self, width=0, height=0):
        self.__check_value(width, "width")
        self.__check_value(height, "height")
        self.__width = width
        self.__height = height

    def __check_value(self, value, atribute):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(atribute))
        if value < 0:
            raise ValueError("{:s} must be >= 0".format(atribute))
        return False

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__check_value(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__check_value(value, "height")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        rows = "#" * self.width
        return (rows + "\n") * (self.height - 1) + rows

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
