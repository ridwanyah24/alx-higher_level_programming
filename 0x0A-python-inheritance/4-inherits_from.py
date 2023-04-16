#!/usr/bin/python3
"""this class returns true if an
objects is an instance of a class that inherits
directly or indirectly from the specified class otherwise false"""


def inherits_from(obj, a_class):
    if issubclass(obj, a_class):
        return True
    else:
        return False
