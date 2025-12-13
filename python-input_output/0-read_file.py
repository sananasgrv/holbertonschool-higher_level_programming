#!/usr/bin/python3
"""Documentation"""


def read_file(filename=""):
    """FUnction documentation"""

    with (open(filename, encoding="utf-8") as f):
        data = f.read()
        return data
