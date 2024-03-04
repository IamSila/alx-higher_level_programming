#!/usr/bin/python3
"""function called write_file
    args:
        filename - the file to write
        text - the text to write to the file
"""


def write_file(filename="", text=""):
    """
    open a file named filename and write the contents
    of text to the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
