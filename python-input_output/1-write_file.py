#!/usr/bin/python3
"""Document"""

def write_file(filename="", text=""):
    with open(filename, encoding="utf-8")  as f:
        print(f.write(text), end="")