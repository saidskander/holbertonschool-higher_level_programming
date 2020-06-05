#!/usr/bin/python3
"""student"""


class Student:
    """class for Student"""
    def __init__(self, first_name="", last_name="", age=""):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json dict"""
        a_dict = {}
        if attrs is None:
            return self.__dict__
        for x in attrs:
            if hasattr(self, x):
                a_dict[x] = getattr(self, x)
        return a_dict
