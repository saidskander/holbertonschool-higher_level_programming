#!/usr/bin/python3
"""adds and save"""
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
open("add_item.json", "a")
try:
    x = load_from_json_file("add_item.json")
except ValueError:
    x = []
save_to_json_file(x + sys.argv[1:], "add_item.json")
