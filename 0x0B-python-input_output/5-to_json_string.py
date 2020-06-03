#!/usr/bin/python3
"""representation of an object: JSON is the best"""


import json


def to_json_string(my_obj):
    """json"""
    jsonresult = json.dumps(my_obj)
    return jsonresult
