#!/usr/bin/python3
"""function named inherits_from"""


def inherits_from(obj, a_class):
    """checks if obj is a subclass of a_class
        args:
        obj - value with the value to check
        a_class - the parent class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
