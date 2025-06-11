#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    a_dictionaryKeys = sorted(list(a_dictionary))

    for key in a_dictionaryKeys:
        print("{}: {}".format(key, a_dictionary[key]))
