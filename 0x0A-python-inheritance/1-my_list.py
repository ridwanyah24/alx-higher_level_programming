#!/usr/bin/python3
""" this class inherits from the list class"""


class MyList(list):
    """ this function is just a self function"""
    def __init__(self):
        pass

    def print_sorted(self):
        """ prints a list in sorted ascending order"""
        print(sorted(self))
