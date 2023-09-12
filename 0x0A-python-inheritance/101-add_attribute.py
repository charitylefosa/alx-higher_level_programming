#!/usr/bin/python3
"""adds a new attribute to object if possible"""


def add_attribute(obj, name, value):
    """adds attribute"""
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
