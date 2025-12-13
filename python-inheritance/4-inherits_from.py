#!/usr/bin/python3
"""Documentation"""


def inherits_from(obj, class_a):
    """Documentation of function"""
    obj_class = type(obj)
    if issubclass(obj_class, class_a) and obj_class != class_a:
        return True
    return False
