#!/usr/bin/python3
"""
A Rectangle Class with private instance attributes width, height,
and public methods for area, perimeter, and string representation.
"""


class Rectangle():
    """
    Rectangle class represents a rectangle with width and height.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle object with specified width and height.

        Parameters:
        - width (int): Width of the rectangle (default is 0).
        - height (int): Height of the rectangle (default is 0).
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        - int: Area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
        - int: Perimeter of the rectangle.
        """
        if (self.__width == 0 or self.__height == 0):
            return 0

        return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on the area
          Args:
            - rect_1: Rectangle
            - rect_2: Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        return rect_2

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        - str: String representation of the rectangle using '#' characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        final = [symbol * self.__width for h in range(self.__height)]

        return '\n'.join(final)

    def __repr__(self):
        """
        Return a string representation of the rectangle for object recreation.

        Returns:
        - str: String representation of the rectangle as valid Python code.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
    Destructor method for the Rectangle class.

    Returns:
    - None
    """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
        - int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Parameters:
        - value (int): New width value.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
        - int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Parameters:
        - value (int): New height value.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(width=size, height=size)
