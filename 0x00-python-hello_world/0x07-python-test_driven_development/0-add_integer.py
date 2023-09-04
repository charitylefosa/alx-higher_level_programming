#!/usr/bin/python3
""" A module for a function that adds 2 integers"""

def add_integer(a, b=98):
    """ returns the addition of a and b
    
    a and b must be intergers or floats

    Raise a TypeError if they are any other type

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
