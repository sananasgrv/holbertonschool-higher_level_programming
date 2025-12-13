#!/usr/bin/python3
"""Adds all arguments to a Python list, then saves them to a JSON file"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

items = load_from_json_file(filename)
save_to_json_file(items, filename)
