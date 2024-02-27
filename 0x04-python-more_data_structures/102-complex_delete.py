#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    dict_keys = list(a_dictionary.keys())

    for key in dict_keys:
        if value == a_dictionary.get(key):
            del a_dictionary[key]
    return a_dictionary
