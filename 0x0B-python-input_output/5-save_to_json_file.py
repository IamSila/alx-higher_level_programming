#!/usr/bin/python3
"""
function called save_to_json_file
saves a JSON format to a file
args:
    my_obj - obj to convert to JSON
    filename - where to save the JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """convert data to a json format and
    save to a file called filename
    """
    with open(filename, mode='w') as a_file:
        a_file = json.dumps(my_obj)
        return a_file
