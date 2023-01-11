#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """print a dictionary by ordered keys"""
    sorted_list = sorted(a_dictionary)
    for key value in sorted_list:
        print("{}: {}".format(key, value))
