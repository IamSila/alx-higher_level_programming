#!/usr/bin/python3
"""a chilld square class that inherits from a parent class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """initializing the attributes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
