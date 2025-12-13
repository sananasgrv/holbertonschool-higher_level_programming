#!/usr/bin/python3
def is_kind_of_class(obj, class_a):
    obj_class = type(obj)
    if issubclass(obj_class, class_a):
        return True
    return False