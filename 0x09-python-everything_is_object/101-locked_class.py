#!/usr/bin/python3

class LockedClass:
    """
    LockedClass is a class that restricts the set
    of attributes itsinstances can have.

    Attributes:
    __slots__ (tuple): A tuple specifying the allowed attributes
    for instances of the class.
    """

    __slots__ = ('first_name',)
