#!/usr/bin/python3
""" Base Class"""


import json
import csv
import os


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """base initialization"""
        if id is None:
            base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id


    @statcismethod
    def to_json_string(list_dictionaries):
        ""Returning json
