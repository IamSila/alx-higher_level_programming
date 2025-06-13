#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    """returns all values in a list  multiplied by a number without using a loop"""
    return list(map(lambda x: x * number, my_list))
