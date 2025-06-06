#!/usr/bin/python3


def max_integer(my_list=[]):
    """returns the max value inside a list"""
    length = len(my_list)
    if length > 0:
        for i in range(0, length - 1):
            if my_list[i] > my_list[i + 1]:
                return my_list[i]
