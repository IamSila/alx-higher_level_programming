#!/usr/bin/python3


def element_at(my_list, idx: int):
    """returns an element at index position specified"""
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]
