#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """delete value at the given index position"""
    length = len(my_list)
    if idx < 0 or idx >= length:
        return my_list
    else:
        del my_list[idx]
    return my_list
