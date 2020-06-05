#!/usr/bin/python3
"""Json leoads an object file”"""
import json


def load_from_json_file(filename):
    """creating object from a json File"""
    with open(filename, encoding="utf-8") as File:
        return json.load(File)
