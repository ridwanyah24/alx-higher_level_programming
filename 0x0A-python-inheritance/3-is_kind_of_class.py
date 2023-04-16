#!/usr/bin/python3


""" this function returns a true or false if  the object is an
    instance of a class that inherited from it"""
def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
