#!/usr/bin/python3

"""class Square """

class Square:
    """ defines a square
    Args:
        size(int): the size of the square
    """
    def __init__(self, size=0):
        """Initializes the square"""
        self.size = size

    @property
    def size(self):
        """Gets/Sets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """ Prints the square with #s"""

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("")
                for j in range(self.__size):
                    print("#", end="")
        print("")
