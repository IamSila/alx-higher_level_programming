#!/usr/bin/python3

"""create a class Square"""


class Square:
    """Instantiation with optional size
        args:
            size - is the size of the square
    """
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        """returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets properties for the properties of size
        args:
            value- is the size of the square

        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")

        elif (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def area(self):
        """method to return the area"""
        return self.__size * self.__size

    def my_print(self):
        """prints area in the form of #"""
        if self.__size == 0:
            print()
        else:
            for area in range(self.__size):
                print("#" * self.__size)
