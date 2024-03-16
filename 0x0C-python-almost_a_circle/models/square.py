#!/usr/bin/python3
"""a class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super()._init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        """
        on print it returns the following representation
        """
        return
        "[Square ({})]  {}/{} - {}".format(self.id, self.x, self.y, self.width)
