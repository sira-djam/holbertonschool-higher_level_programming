#!/usr/bin/python3
"""function that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):

    with open(filename, 'r') as file:
        """
        Load the JSON content of the file and create the corresponding
        Python object
        """
    return json.load(file)
