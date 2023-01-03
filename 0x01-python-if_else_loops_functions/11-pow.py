#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        b = -b
        return 1 / a ** b
    else:
        return a ** b
