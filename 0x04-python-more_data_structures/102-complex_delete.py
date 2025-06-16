#!/usr/bin/python3
dictionary = {"lang": "C", "track": "Low", "pref": "C", "ids": [1, 2, 3]}


def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    dictionary_keys = list(a_dictionary)
    for i in dictionary_keys:
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary


result = complex_delete(dictionary, "C")
print(result)
