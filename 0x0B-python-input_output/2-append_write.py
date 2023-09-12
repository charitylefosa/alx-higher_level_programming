#!/usr/bin/python3
"""composed of function that appends a string"""


def append_write(filename="", text=""):
    """returns num of chars added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
