#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length_of_list = len(my_list)
    if idx < 0:
        print("{}".format(my_list))
    elif idx >= length_of_list:
        print("{}".format(my_list))
    else:
        my_list[idx] = element
        print("{}".format(my_list))
