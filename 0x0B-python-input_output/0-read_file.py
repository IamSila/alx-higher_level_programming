#!/usr/bin/python3
"""this function is called read_file"""


def read_file(filename="", mode='r'):
    """read and return the contents of the file"""
    with open(filename, encoding="utf-8") as a_file:
        contents = a_file.read()
        """print the contents"""
        print(contents, end="")
