#!/usr/bin/python3
"""

matrix_divided: function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix
    Args:
        matrix (list): matrix of int or float
        div (int): Number
    Returns:
        list: a new matrix
    """
    listMsj = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)) or div != div:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix:
        raise TypeError(listMsj)
    if type(matrix) is not list:
        raise TypeError(listMsj)
    if not all(isinstance(x, list) for x in matrix):
        raise TypeError(listMsj)
    if not all(len(row) for row in matrix):
        raise TypeError(listMsj)
    if not all([all(isinstance(val, (int, float)) for val in row)
                for row in matrix]):
        raise TypeError(listMsj)
    if len(set([len(row) for row in matrix])) is not 1:
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(x / div, 2) for x in row] for row in matrix]


