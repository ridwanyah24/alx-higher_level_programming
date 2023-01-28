#!/usr/bin/python3
class Square:
    """this class belongs to a square"""
    def __init__(self, size=0):
        self.__size = size

        if (type(self.__size) != int):
            raise TypeError("size must be integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")
