#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id[int]: The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """It returns a json representation
        of the list_dictionaries argument
        Args:
            list_dictionaies (list):  a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        my_file = cls.__name__ + ".json"
        with open(my_file, "w", encoding="utf-8") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [key_value.to_dictionary()
                              for key_value in list_objs]
                json_file.write(Base.to_json_string(list_dicts))
