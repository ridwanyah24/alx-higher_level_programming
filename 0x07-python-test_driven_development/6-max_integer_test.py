#!/bin/usr/python3


def max_integer(list=[]):
    """ returns the maximum of a list of integers
        if the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
