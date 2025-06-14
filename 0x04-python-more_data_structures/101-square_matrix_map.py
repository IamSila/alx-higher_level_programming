#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    """return squared values of a matrix"""
    new_matrix = matrix.copy()

    return list(map(lambda y: list(map(lambda x: x**2, y)), matrix))
