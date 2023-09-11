#!/usr/bin/python3
"""Contains Empty Class BaseGeometry"""


class BaseGeometry:
    """Empty class"""

    def area(self):
        """raises an Exception with the message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".fornat(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
