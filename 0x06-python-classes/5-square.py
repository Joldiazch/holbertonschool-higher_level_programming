#!/usr/bin/python3
class Square:
    def __init__(self, size_of_square=0):
        if type(size_of_square) is not int:
            raise TypeError('size must be an integer')
        elif size_of_square < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size_of_square

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
