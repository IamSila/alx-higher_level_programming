#!/usr/bin/python3

def element_at(my_list, idx):
    length_of_list = len(my_list)
    if idx < 0:
        return None
    elif idx >= length_of_list:
        return None
    else:
        return my_list[idx]
