#!/usr/bin/python3

"""class called print_sorted"""


class MyList(list):
    """prints the sorted list
        args:
            list - holds the unsorted list
    """
    def __init__(self):
        """initializing the object"""
        super().__init__()
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
