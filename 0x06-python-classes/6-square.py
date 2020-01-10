#!/usr/bin/python3
class Square:
    def __init__(self, size_of_square=0, position=(0, 0)):
        if type(size_of_square) is not int:
            raise TypeError('size must be an integer')
        elif size_of_square < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size_of_square
        if type(position) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (type(position[0]) is not int) and (type(position[1]) is not int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (position[0] < 0) or (position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (type(value[0]) is not int) and (type(value[1]) is not int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (position[0] < 0) or (position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
        pass

    def my_print(self):
        if self.size == 0:
            print()
        print("\n" * self.position[1], end="")
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
