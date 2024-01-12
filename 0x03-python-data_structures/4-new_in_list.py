def new_in_list(my_list, idx, element):
    list_copy = my_list.copy()
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        list_copy[idx] = element
        return list_copy
