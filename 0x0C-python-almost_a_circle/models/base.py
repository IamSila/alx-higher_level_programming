#!/usr/bin/python3

"""This is a class called base class to act as the parent class"""


class Base(object):
    """Defining the attributes of the class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializing the class attributes
        """
        if self.id is not None:
            self.id = id
        else:
            self.id = self.__nb_objects = + 1
