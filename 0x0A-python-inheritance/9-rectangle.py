#!/usr/bin/python3
""" Class Rectangle that defines a rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """initializes a new Rectangle
        Area:
           width (int): the widht of the rec
           height (int): the height of the rec
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rec"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the str() and print() representation of a rec"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
