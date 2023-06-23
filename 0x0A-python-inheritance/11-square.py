#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents the square class"""

    def __init__(self, size):
        """Initializes the class
        Args:
           size: the size of the class
        """
        self.integer_validator("size", size)
        self.__init__(self, size, size)
        self.__size = size
