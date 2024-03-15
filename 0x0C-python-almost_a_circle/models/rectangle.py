#!/usr/bin/python3

"""defines a Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle model.

    This class inherits from the Base class

    Private instance Attributes:
       __width (int): The width of the rectangle.
       __height (int): The height of the rectangle
       x -
       y -
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width(int): The width of the rectangle
            height - height of the rectangle
            x - x of the rectangle
            y - y of the rectangle
            id - is the id of the rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


        @property
        def width(self):
            """width of the rectangle"""
            return self.__width

        @property
        def height(self):
            """
            height of the rectangle
            """
            return self.__height

        @property
        def x(self):
            """x of the rectangle"""
            return self.__x

        @property
        def y(self):
            """y of the rectangle"""
            return self.__y

        @width.setter
        def width(self, value):
            """set width = value"""
            self.__width = value

        @height.setter
        def height(self, value):
            """set height = value"""
            self.__height = value

        @x.setter
        def x(self, value):
            """set x = value"""
            self.__x = value

        @width.setter
        def y(self, value):
            """set y = value"""
            self.__y = value
