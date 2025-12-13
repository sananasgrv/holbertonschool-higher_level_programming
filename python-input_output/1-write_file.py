#!/usr/bin/python3
"""Document"""


def write_file(filename="", text=""):
    """Documented"""

    with open(filename, "w", encoding="utf-8")  as f:
        return f.write(text)
