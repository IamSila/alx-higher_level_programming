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
    filename = json.dumps(my_obj)
