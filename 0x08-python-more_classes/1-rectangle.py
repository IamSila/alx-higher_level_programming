#!/usr/bin/python3
"""Rectangle class with rectangle attributes"""


class Rectangle():
    """Has xtics of a rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the value of the width
            args:
                value: int holding width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height
            args:
                - value - int value for the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be an integer")
        self.__height = value