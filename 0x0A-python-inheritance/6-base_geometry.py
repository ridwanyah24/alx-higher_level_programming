#!/usr/bin/python3
""" this class does nothing"""


class BaseGeometry():
    pass


""" this class does nothing based on the previous class that does nothing as
well"""


class BaseGeometry(BaseGeometry):
    """ this function calculates the area of a shape"""
    def area(self):
        raise Exception("area() is not implemented")
