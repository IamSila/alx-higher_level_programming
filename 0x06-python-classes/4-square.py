#!/usr/bin/python3
"""A class carring the properties and the methods of a square"""


class Square:
    def __init__(self, size=0):
        """Initialize a Square instance with a given size.

        Args:
            size (int): The size of the square (default is 0).
        """
        # Validate and set the size attribute using the setter method
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        # Validate that size is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Validate that size is greater than or equal to 0
        if value < 0:
            raise ValueError("size must be >= 0")

        # Set the size attribute
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
