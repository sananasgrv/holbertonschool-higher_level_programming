#!/usr/bin/python3
"""Doc"""
import json


def save_to_json_file(my_obj, filename):
    """Doc"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(json.loads(my_obj))
