#!/usr/bin/python3
"""base all other classes"""


class Base:
    """test check for doc string"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
