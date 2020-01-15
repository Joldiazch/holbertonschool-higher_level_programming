#!/usr/bin/python3
"""class Rectangle that defines a Rectangle"""


class Rectangle:
    """class Rectangle that defines a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__check_value(width, "width")
        self.__check_value(height, "height")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        rows = str(self.print_symbol) * self.width
        return (rows + "\n") * (self.height - 1) + rows

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectanglex")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
