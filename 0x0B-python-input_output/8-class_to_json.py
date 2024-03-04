#!/usr/bin/python3
""" function named class_to_json
args: obj - the class instance to convert
to a dictionary
"""


def class_to_json(obj):
    """Represent object as a dictionary"""
    return obj.__dict__
