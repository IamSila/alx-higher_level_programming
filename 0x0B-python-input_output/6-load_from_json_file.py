#!/usr/bin/python3
"""
function called load_from_file
args:
    filename - file to load from
"""
import json


def load_from_json_file(filename):
    """load from a file called filename"""
    with open(filename) as a_file:
        return json.load(a_file)
