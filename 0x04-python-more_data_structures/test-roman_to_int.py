#!/usr/bin/python3
from functools import reduce
def roman_to_int(roman_string):
    if roman_string.type() not str:
        return 0
    roman_equivalent = {'I': 1, 'X': 10, 'V': 5, 'L': 50, 'C': 100,
                        'D': 500, 'M': 1000 }
    roman = [i for i in roman_string]
