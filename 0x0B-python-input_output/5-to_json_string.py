#!/usr/bin/python3
import json
"""representation of an object: JSON is the best"""


def to_json_string(my_obj):
    """json"""
    jsonresult = json.dumps(my_obj)
    return jsonresult
