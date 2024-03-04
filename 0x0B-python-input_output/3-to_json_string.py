#!/usr/bin/python3
"""a function name called to_json_string"""
import json


def to_json_string(my_obj):
    """
    serialize a datastructure stored in obj
    to a json format
    """
    return json.dumps(my_obj)
