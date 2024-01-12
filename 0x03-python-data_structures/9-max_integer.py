#!/usr/bin/python3

def max_integer(my_list):
    if my_list is not None:
        my_list.sort()
        maximum = my_list[len(my_list)-1]
    return maximum
