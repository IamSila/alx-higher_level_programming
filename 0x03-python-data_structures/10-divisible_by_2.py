#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list"""
    new_list = []
    if my_list:
        for i in my_list:
            if i % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
    return new_list
