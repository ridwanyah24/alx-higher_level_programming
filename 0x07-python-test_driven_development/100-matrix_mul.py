#!/bin/usr/python3


def matrix_mul(m_a, m_b):
    """ this function multiplies two matrices together"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list)for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a ==[[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(ele, int) or isinstance(ele, float)) for ele in
               [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")


    if not all((isinstance(ele, int) or isinstance(ele, float)) for ele in
                [num for row in m_a for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    product_matrix = []
    for i in range(len(m_a)):
        product_row = []
        for j in range(len(m_b[0])):
            product_element = 0
            for k in range(len(m_b)):
                product_element = product_element + m_a[i][k]*m_b[k][j]

            product_row.append(product_element)

        product_matrix.append(product_row)

    return (product_matrix)

#    i = 0
#    for row in range(len(m_a)):
#        for column in range(len(m_b)):
#            new_mat = []
#            new_mat.append((m_a[row][i] * m_b[column][i]) +
#                           (m_a[row][i+1] + m_b[column + 1][i]))
#            i += 1
#        mat.append(new_mat)
