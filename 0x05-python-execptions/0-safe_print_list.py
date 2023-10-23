#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ids = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            ids += 1
    except IndexError:
        pass
    print("")
    return ids
