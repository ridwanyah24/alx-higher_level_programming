#!/usr/bin/python3

"""class square which defines a square"""

class Square:
    """ This class defines a square

    Args:
        size(int): the size of the square

    Methods:
          size(self): getter methof to get the size
          size(self, value): setter method to set the size with value
    """
    def __init__(self, size=0):
        """ Initializes the square"""
        self.size = size


    @property
    def size(self):
        """ get/ set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")


    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)
