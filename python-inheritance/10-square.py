#!/usr/bin/python3
"""Defines a Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle from BaseGeometry"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
    def area(self):
        return self.__size * self.__size
