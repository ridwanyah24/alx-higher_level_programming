#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry"""


    def __init__(self, width, height):
        """Initializes a new Rec

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rec
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

        BaseGeometry.__init__(self)
