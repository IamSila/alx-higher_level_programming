#!/usr/bin/python3
"""creating a class square"""


class Square:
    """instantiation method

        Args:
            self - default name argument

    """

    def __init__(self, size=0, position=(0, 0)):
        """args:
                size - optional variable to store size of the square
                position - to set the position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieve the size of the object"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the attributes of the objects in this method"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """setter for the position variable"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """returns the area of the square object"""
        return self.__size * self.__size

    def my_print(self):
        """Method to print a Square with spaces"""
        if (self.__size == 0):
            print()
        else:
            for blank in range(self.position[1]):
                print()
            for rows in range(self.__size):
                print(" " * self.position[0], end='')
                print("#" * self.__size)
