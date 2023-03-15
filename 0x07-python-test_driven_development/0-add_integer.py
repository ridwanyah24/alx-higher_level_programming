#!/usr/bin/python3
""" new stuff """
def add_integer(a, b=0):
    """ Returns the addition of a and b
    Float arguments are converted to ints before addition is done


    Raises:
    TypeError: if either a or b is a non-integer and non-float.

    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance (b, int) and not isinstance (b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
