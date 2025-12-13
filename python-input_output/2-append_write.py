#!/usr/bin/python3
"""Documentation"""


def append_write(filename="", text=""):
    """Documentation"""

    with open(filename, "a", encoding="utf-8")as f:
        return f.write(text)
