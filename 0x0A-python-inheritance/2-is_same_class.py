#!/usr/bin/python3


def is_same_class(obj, a_class):
    """ this class returns true if the object is exactly an instance of the
    specified class otherwise false"""
    if type(obj) == a_class:
        return True
    else:
        return False
