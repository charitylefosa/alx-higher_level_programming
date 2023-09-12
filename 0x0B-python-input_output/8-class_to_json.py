#!/usr/bin/python3
"""composed of function class_to_json"""


def class_to_json(obj):
    """ returns dictionary representationof simple data structure"""
    return obj.__dict__
