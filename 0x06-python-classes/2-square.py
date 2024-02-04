#!/usr/bin/python3
"""This class is called a square and will have xtics/properties of squares"""


class Square:
    """This method initializes the class
    
    Initialize a Square instance with a given size.

        Args:
            size (int): The size of the square (default is 0).
    """
    def __init__(self, __size=0):
        self.__size = __size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
