#!/usr/bin/python3
"""Documentation"""


def inherits_from(obj, class_a):
    """Documentation of function"""
    obj_class = type(obj)
    if issubclass(class_a, obj_class):
        return True
    return False
