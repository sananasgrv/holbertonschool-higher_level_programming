#!/usr/bin/python3
def common_elements(set_1, set_2):
    list_1 = list(set_1)
    list_2 = list(set_2)
    sum_sets = set_1 + set_2
    sum_list = list_1 + list_2
    uniq_list = []
    for i in range(sum_list):
        if sum_list[i] != sum_sets:
            uniq_list.append(sum_list[i])
    return uniq_list
