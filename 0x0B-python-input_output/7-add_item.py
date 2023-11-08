#!/usr/bin/python3
""" 7. Load, add, save """
import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """ add all arguments """
    if os.path.exists('add_item.json'):
        python_list = load_from_json_file('add_item.json')
        argv = sys.argv[1:]
        python_list.extend(argv)
        save_to_json_file(python_list, 'add_item.json')
    else:
        save_to_json_file(sys.argv[1:], 'add_item.json')


add_item()
