#!/usr/bin/python
"""createa fonction writea object on the fileto use json"""
import json


def save_to_json_file(my_obj, filename):
    """_summary_

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """    
    with open(filename, 'w') as outfile:
        json.dump(my_obj, outfile)
