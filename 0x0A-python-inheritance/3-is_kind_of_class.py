#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """ this function returns a true or false if  the object is an instance of the class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
