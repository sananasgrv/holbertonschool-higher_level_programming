#!/usr/bin/env python3
def islower(c):
    if 97 <= ord(c) <= 122:  # ASCII range for 'a' to 'z'
        return True
    else:
        return False
