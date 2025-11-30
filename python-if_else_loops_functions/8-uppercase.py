#!/usr/bin/python3
def uppercase(char):
    if 'a' <= char <= 'z':  
        return chr(ord(char) - 32)
    return char