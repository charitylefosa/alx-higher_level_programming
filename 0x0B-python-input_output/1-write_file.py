#!/usr/bin/python3
"""composed of fucntion write_file"""


def write_file(filename="", text=""):
    """returns num of chars written to filename from text"""
    with open(filename, "w", encoding="utf=8") as f:
        return f.write(text)
