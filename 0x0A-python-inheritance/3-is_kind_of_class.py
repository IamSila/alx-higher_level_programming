#!/usr/bin/python3

"""function called is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """checks if obj is an instance
    of a_class
    args:
        obj - the variable to check
        a_class - the parent class
    """
    return isinstance(obj, a_class)
