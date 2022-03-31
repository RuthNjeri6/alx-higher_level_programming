#!/usr/bin/python3
""" Divide items in a Matrix"""


def matrix_divided(matrix, div):
    """ Function to divide elements of a matrix after validation"""
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    elif type(div) is int or type(div) is float:
        div = div
    else:
        raise TypeError('div must be a number')
    length = len(matrix[0])
    new_matrix = []
    for sublist in matrix:
        new_sublist = []
        if len(sublist) != length:
            raise TypeError('Each row of the matrix must have the same size')
        for val in sublist:
            if type(val) is not int and type(val) is not float:
                raise TypeError('matrix must be a matrix \
                    (list of lists) of integers/floats')
            elif type(val) is int or type(val) is float:
                quotient = round(val / div, 2)
                new_sublist.append(quotient)
            else:
                raise TypeError('matrix must be a matrix \
                    (list of lists) of integers/floats')
        new_matrix.append(new_sublist)
    return new_matrix
