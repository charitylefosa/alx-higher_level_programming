#!/usr/bin/python3
"""composed of function from_json_string """
import json


def from_json_string(my_str):
    """ returns Python object representation of a JSON string"""
    return json.loads(my_str)
