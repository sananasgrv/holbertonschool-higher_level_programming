#!/usr/bin/python3
def no_c(my_string):
    my_string_list=list(my_string)

    new_string=""
    for i in my_string_list:
        if i == "c" or i == "C":
            pass
        else:
            new_string+=(i)
    return  new_string