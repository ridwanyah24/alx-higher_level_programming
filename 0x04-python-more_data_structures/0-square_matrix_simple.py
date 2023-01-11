#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda x: x**2, [y[i] for y in matrix for i in
                                           range(len(matrix))]))
    m = []
    while new_matrix != []:
        m.append(new_matrix[:3])
        new_matrix = new_matrix[3:]
    return m
