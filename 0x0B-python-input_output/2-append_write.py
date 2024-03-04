#!/usr/bin/python3

"""
this is a function append_write
args:
    filename - name of the file to append to
    text - text to be used for appending

"""


def append_write(filename="", text=""):
    """opening the file and appending contents to it"""
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
