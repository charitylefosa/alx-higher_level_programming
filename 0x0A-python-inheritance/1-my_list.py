#!/usr/bin/python3
"""New class"""


class MyList(list):
    """class that inherits list"""

    def print_sorted(self):
        """ function that prints a sorted list"""
        print(sorted(self))
