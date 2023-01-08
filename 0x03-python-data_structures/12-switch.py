#!/usr/bin/python3
a = 89
b = 10
lambda x: (x = a, a = b, b = x)
print("a={:d} - b={:d}".format(a, b))
