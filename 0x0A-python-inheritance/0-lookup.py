#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of attributes and methods of the input object.

    Parameters:
    - obj: Any Python object

    Returns:
    - List of strings containing attribute and method names of object.
    """
    return dir(obj)
