#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    myKeys = list(a_dictionary.keys())
    myKeys.sort()
    sd = {i: a_dictionary[i] for i in myKeys}
    for i in sd.keys():
        print("{}: {}".format(i, sd.get(i)))
