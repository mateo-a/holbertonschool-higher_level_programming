#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new = []
    try:
        new = [[x ** 2 for x in row] for row in matrix]
    except TypeError:
        new = [x ** 2 for x in matrix]
    return (new)
