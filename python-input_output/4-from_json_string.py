#!/usr/bin/python3
"""use json load"""
import json



def from_json_string(my_str):
    from io import StringIO
    """_summary_

    Args:
        my_str (_type_): _description_

    Returns:
        _type_: _description_
    """

    return json.dumps(my_str)
