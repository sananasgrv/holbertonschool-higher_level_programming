#!/usr/bin/python3
"""Doc of the module"""
import json


def class_to_json(obj):
    """Doc of the function"""

    return json.dumps(obj.__dict__)