#!/usr/bin/python3
"""Define a class Square with methods and attributes ans methods of a square"""


class Square():
    """the main method of the class"""
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns the area of an object square"""
        return self.__size ** 2
