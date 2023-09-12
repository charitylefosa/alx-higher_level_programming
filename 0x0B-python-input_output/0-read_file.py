#!/usr/bin/python3
"""composed of text reading file function"""


def read_file(filename=""):
    """prints contents of a UTB8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
