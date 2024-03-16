#!/usr/bin/python3
"""a class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.with the following arguments

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """

        super()._init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        """
        on print it returns the following representation
        """
        return
        "[Square ({})]  {}/{} - {}".format(self.id, self.x, self.y, self.width)
