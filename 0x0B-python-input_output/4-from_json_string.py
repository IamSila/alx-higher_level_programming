#!/usr/bin/python3
"""
function called from_json_string(my_str)
args:
    my_str - json format to convert to python datastructure
"""
import json


def from_json_string(my_str):
    """convert my_str to a python data structure"""
    return json.loads(my_str)
