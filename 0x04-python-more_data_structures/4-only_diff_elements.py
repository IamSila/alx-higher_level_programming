#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """returns only different elements between the set_1 and set_2"""
    results = set_1 ^ set_2
    return results
