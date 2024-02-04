#!/usr/bin/python3
"""This class is called a square and will have xtics/properties of squares"""


class Square:
    """This method initializes the class"""
    def __init__(self, __size=0):
        self.__size = __size

    def checker(self, __size):
        """This class checks if size is a int and if size is greater than 0"""
        if (self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
