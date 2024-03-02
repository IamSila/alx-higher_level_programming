#!/usr/bin/python3
"""function named is_same_class"""


def is_same_class(obj, a_class):
    """return True or False
        args:
            object - variable holding a value
            a_class - type to check against    
    """
    return isinstance(obj, a_class)

