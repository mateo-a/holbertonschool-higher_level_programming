#!/usr/bin/python3
"""

function that multiplies 2 matrices

"""


def check_args(matrix, name):
    """Check values"""
    if not isinstance(matrix, list):
        raise TypeError("{} must be a list".format(name))
    rows_length = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("{} must be a list".format(name))
        rows_length.append(len(row))
        for val in row:
            if not isinstance(val, (float, int)) or type(val) is bool:
                raise TypeError("{} should contain only integers or floats"
                                .format(name))

    if len(rows_length) == 0 or max(rows_length) == 0:
        raise ValueError("{} can't be empty".format(name))

    if max(rows_length) != min(rows_length):
        raise TypeError("each row of {} must should be of the same size"
                        .format(name))
    return True


def matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices
    Arguments:
        m_a (list): matrix
        m_b (list): matrix
    Returns:
       new matrix
    """
    check_args(m_a, "m_a")
    check_args(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new = [[sum(m_a[j][i] * m_b[i][k] for i in range(len(m_b)))
            for k in range(len(m_b[0]))] for j in range(len(m_a))]
    return (new)
