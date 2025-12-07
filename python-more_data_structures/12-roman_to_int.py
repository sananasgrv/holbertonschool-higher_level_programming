#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    rome_dict= {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50 ,'C' : 100, 'D' : 500, 'M' : 1000}
    num = 0
    for i in range(len(roman_string)):
        if roman_string[i] >= roman_string[i-1]:
            num += rome_dict.get(roman_string[i])
        else:
            num -= rome_dict.get(roman_string[i])
    return num
