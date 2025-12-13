#!/usr/bin/python3
"""Documentation"""


def inherits_from(obj, class_a):
    """Documentation of function"""
    obj_class = type(obj)
    if issubclass(class_a, obj_class) and obj_class != class_a:
        return True
    return False
