#!/usr/bin/python3
"""
This program print a message with the next format:
  My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):

    """
    This function print the next message: My name is <first name> <last name>
    Args:
      - first name: str holding the first name
      - last name: str (Optional) holding last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
