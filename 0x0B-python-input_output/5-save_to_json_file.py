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
    with open(filename, mode='w', encoding='utf-8') as a_file:
        """write the contents to filename"""
        json.dump(my_obj, a_file)
