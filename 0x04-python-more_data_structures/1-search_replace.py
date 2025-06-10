#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """replace all occurences of an element by another in a new list"""
    new_list = my_list.copy()
    length = len(my_list)

    for index in range(length):
        if new_list[index] == search:
            new_list[index] = replace
    return new_list
