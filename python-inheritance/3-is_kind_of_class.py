#!/usr/bin/python3
"""Documentation"""


def is_kind_of_class(obj, class_a):
    """Documentation"""

    obj_class = type(obj)
    if issubclass(obj_class, class_a):
        return True
    return False
