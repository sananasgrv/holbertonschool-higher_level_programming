#!/usr/bin/python3
"""Document"""

def write_file(filename="", text=""):
    """Documented"""

    with open(filename, "w")  as f:
        print(f.write(text), end="")