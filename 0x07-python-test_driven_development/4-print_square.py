#!/usr/bin/python3
""" Module composed of a function that prints a square with the character # """


def print_square(size):
    """ Prints a square with # character

    Args:
        size(int): Height/width of square

    Raise:
        TypeError: if size is not an integer number
                   if size is a float and is less than 0
        ValueError: if size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
