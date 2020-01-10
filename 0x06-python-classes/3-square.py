#!/usr/bin/python3
class Square:
    """class Square that defines a square by: (based on 0-square.py)
    Attributes:
        size_of_square (int): Description of `attr1`.

    """
    def __init__(self, size_of_square=0):
        if type(size_of_square) is not int:
            raise TypeError('size must be an integer')
        elif size_of_square < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size_of_square

    def area(self):
        return self.__size ** 2
