#!/usr/bin/python3
"""composed of function to_json_string"""
import json


def to_json_string(my_obj):
    """function that returns JSON representation of object"""
    return json.dumps(my_obj)
