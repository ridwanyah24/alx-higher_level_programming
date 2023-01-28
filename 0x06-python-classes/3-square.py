#!/usr/bin/python3
"""
this unit is the new square class
"""


class Square:
    """the new square class"""
    def __init__(self, size=0):
        self.__size = size
    def area(self):
        power = pow(self.__size, 2)

        return power
