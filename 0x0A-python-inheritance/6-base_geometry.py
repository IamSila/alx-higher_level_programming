#!/usr/bin/python3

"""a class named BaseGeometry"""


class BaseGeometry(object):
    """describes the attributes and methods
        args:
            object - is the ancestor class in which
            all classes inherit from
    """
    def area(self):
        """should return the area"""
        raise Exception("area() is not implemented")
