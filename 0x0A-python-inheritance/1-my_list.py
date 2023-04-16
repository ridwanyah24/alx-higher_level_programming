#!/usr/bin/python3
""" this class inherits from the list class"""


class MyList(list):
    """ this function is just a self function"""
    def __init__(self):
        pass

    """ this is the main function """
    def print_sorted(self):
        print(sorted(self))
