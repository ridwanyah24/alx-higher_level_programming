#!/usr/bin/python3
"""Defines a class for squares"""


class Square:
    """The Square class"""

    def __init__(self, size=0):

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    """Returns the area of a Square"""
    def area(self):
        return (self.__size * self.__size)


    """Prints a Square"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            i = 0
            while (i < self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
                i += 1
