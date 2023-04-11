#!/usr/bin/python3


def print_square(size):
    """the program prints a number of # into a square
    size: the size of the square and it must be an integer
    size must be an integer otherwise TypeError: size must be an integer
    if size is less than 0, raise a ValueError: size must be >= 0
    if size is a float and is less than 0, raise TypeError: size must be an
    integer
    """

    if (not isinstance(size, int) and not isinstance(size, float)):
        raise TypeError("size must be an integer")

    if (size < 0) and isinstance(size, float):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        for j in range(int(size)):
            print("#", end="")
        print("")
