#!/usr/bin/python3
""" the new square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Representation of a Square Class"""

    def __init__(self, size):
        """Initializes the square class
        Args:
           size (int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
