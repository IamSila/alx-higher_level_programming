#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri_last = triangles[-1]
        temp = [1]
        for i in range(len(tri_last) - 1):
            temp.append(tri_last[i] + tri_last[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
