#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    new_list=[]
    if len(list_a) < 2 or len(list_b) < 2:
        for i in range(2):
            list_a.append(0)
            list_b.append(0)
    for i in range(2):
        new_list.append(list_a[i] + list_b[i])
    new_tuple=tuple(new_list)
    print(new_tuple)