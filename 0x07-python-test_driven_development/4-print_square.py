#!/usr/bin/python3
"""
    this script prints a square interms of hashes
    depending on size of the square
"""


def print_square(size):
    """
        prints a square shape
        args:
            size: the length of the square
    """
    # size must be an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for distance in range(0, size, 1):
        print("#" * size)
