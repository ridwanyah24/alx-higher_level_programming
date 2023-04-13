#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """the function prints firstname and lastname
    the firstname and lastname must be strings otherwise
    Raise: TypeError(Firstname must be a string or lastname must be a string)
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print ("My name is {} {}".format(first_name, last_name) )