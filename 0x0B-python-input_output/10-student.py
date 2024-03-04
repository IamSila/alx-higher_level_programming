#!/usr/bin/python3
"""a class named Student"""


class Student(object):
    """a class describing attributs for students"""
    def __init__(self, first_name, last_name, age):
        """initializing the values"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dictionary of attributes"""
        
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
