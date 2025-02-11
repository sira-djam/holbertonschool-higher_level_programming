#!/usr/bin/python3
"""function that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """
        Load the JSON content of the file and create the corresponding
        Python object
        """
    with open(filename, "r", encoding='utf-8') as file:
            return json.load(file)
