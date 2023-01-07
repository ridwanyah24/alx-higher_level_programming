#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x , y = list(tuple_a), list(tuple_b)
    if len(x) < 3:
        for i in range(2 - (len(x) - 1)):
            x.append(0)
    if len(y) < 3:
        for i in range(2 - (len(y) - 1)):
            y.append(0)

    new_tup = []
    new_tup.append(x[0] + y[0])
    new_tup.append(x[1] + y[1])
    the_list = tuple(new_tup)

    return the_list
