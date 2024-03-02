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

    def integer_validator(self, name, value):
        """runs checks for value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
