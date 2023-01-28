#!/usr/bin/python3
"""
this is the class for the stuff
"""


class Square:
    """this class belongs to a square"""

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
