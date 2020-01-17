#!/usr/bin/python3
"""

Function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices
    Args:
        m_a (list): List
        m_b (list): List
    Returns:
        int: a + b casted to integer
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if m_a == [] or m_a == [[], []] or len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[], []] or len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    try:
        if len(m_a[0]) == 0:
            raise ValueError("m_a can't be empty")
    except Exception:
        raise ValueError("m_a can't be empty")
    try:
        if len(m_b[0]) == 0:
            raise ValueError("m_b can't be empty")
    except Exception:
        raise ValueError("m_b can't be empty")
    length = 0
    for row in m_a:
        if length == 0:
            length = len(row)
        elif length != len(row):
            raise TypeError('each row of m_a must should be of the same size')
        for val in row:
            if not isinstance(val, int) and not isinstance(val, int):
                raise TypeError("m_a should contain only integers or floats")
    length = 0
    for row in m_b:
        if length == 0:
            length = len(row)
        elif length != len(row):
            raise TypeError('each row of m_b must should be of the same size')
        for val in row:
            if not isinstance(val, int) and not isinstance(val, int):
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for x in range(len(m_b[0]))] for n in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_a[0])):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
