#!/usr/bin/python3
"""Comment"""


class Rectangle:
    """Class doc"""
    def __init__(self,width = 0, height = 0):
        self.width = width
        self.height = height

    def width(self, value):
       if not isinstance(value,int):
           raise(TypeError("width must be an integer"))
       elif(self.width <0 ):
           raise(ValueError("width must be >= 0"))
    def height(self, value):
        if not isinstance(value, int):
            raise (TypeError("width must be an integer"))
        elif (self.height < 0):
            raise (ValueError("width must be >= 0"))


