#!/usr/bin/python3
"""composed of function load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates python object from json file"""
    with open(filename) as f:
        return json.load(f)
