#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a:
        return add_tuple(tuple_b, (0, 0))
    if not tuple_b:
        return add_tuple((tuple_a), (0, 0))
    i = tuple_a[0] + tuple_b[0]
    j = 0 if len(tuple_a) == 1 else tuple_a[1]
    j += 0 if len(tuple_b) == 1 else tuple_b[1]
    return (i, j)
