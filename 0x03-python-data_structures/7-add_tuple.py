#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples and returns the sum"""
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    col1 = (tuple_a[0] if len_a > 0 else 0) + (tuple_b[0] if len_b > 0 else 0)
    col2 = (tuple_a[1] if len_a > 1 else 0) + (tuple_b[1] if len_b > 1 else 0)
    return (col1, col2)
