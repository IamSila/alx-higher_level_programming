#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2"""
    new_dictionary = a_dictionary.copy()
    new_dictionaryKeys = list(new_dictionary.keys())

    for key, value in new_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary
