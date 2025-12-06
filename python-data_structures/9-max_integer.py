#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        sorted(my_list)
        return my_list[-1]
    else:
        return (0, None)
