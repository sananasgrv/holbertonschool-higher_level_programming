#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_1 = (set_1 | set_2)
    new_2 = (set_1 & set_2)
    return new_1 - new_2
