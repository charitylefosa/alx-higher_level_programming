#!/usr/bin/python3
"""contains function is_same_class"""


def is_same_class(obj, a_class):
    """function that returns true if the object is exactly\
       an instance of the specified class ; otherwise False"""
    return (type(obj) == a_class)
