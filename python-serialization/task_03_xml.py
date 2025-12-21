#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, "item")
        child.set("key", key)
        child.set("type", type(value).__name__)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for item in root.findall("item"):
        key = item.get("key")
        value_type = item.get("type")
        value_text = item.text

        # Type conversion
        if value_type == "int":
            value = int(value_text)
        elif value_type == "float":
            value = float(value_text)
        elif value_type == "bool":
            value = value_text == "True"
        else:
            value = value_text

        result[key] = value

    return result
