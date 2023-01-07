#!/usr/bin/python3
def no_c(my_string):
    """returns a new string without the char cC"""

    new_string = [x for x in my_string if x != 'c' and x != 'C']
    return("".join(new_string))
