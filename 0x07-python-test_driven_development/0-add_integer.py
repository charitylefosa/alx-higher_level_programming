#!/usr/bin/python3
""" Module composed by a function that adds 2 numbers """


def add_integer(a, b=98):
    """ adding 2 integer and/or float numbers

    Args:
        a: 1st number
        b: 2nd number

    Return:
        Addition of 2 given numbers

    Raise:
        TypeError: If a or b aren't integer and/or float numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
