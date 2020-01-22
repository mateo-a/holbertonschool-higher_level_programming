#!/usr/bin/python3
"""

Script that adds all arguments to a Python list, and then save them to a file

"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    content = load_from_json_file("add_item.json")
except FileNotFoundError:
    content = []
for arg in sys.argv[1:]:
    content.append(arg)
save_to_json_file(content, "add_item.json")
