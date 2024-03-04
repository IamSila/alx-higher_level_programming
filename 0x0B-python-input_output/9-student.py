#!/usr/bin/python3
"""a class named Student"""


class Student(object):
    """a class describing attributs for students"""
    def __init__(self, first_name, last_name, age):
        """initializing the values"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return a dictionary of attributes"""
        return self.__dict__
