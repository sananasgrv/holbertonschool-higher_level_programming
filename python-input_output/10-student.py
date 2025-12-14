#!/usr/bin/python3
"""Doc"""


class Student():
    """Doc of class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self,  attrs=None):
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return attrs.__dict__
        return self.__dict__
