#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    dictionary_keys = list(a_dictionary.keys())
    for key in dictionary_keys:
        if value == a_dictionary.get(key):
            del a_dictionary[key]
    return a_dictionary
