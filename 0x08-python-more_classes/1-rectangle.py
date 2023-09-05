#!/usr/bin/python3
"""
Defines class Rectangle
"""


class Rectangle:
    """
    Rectangle class representation
    """
    def __init__(self, width=0, height=0):
        """ initialize rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        method that returns the value of the width

        Returns:
            rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        defines width

        args:
            value: width

        raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        method that returns the value of the height

        Returns:
            rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        defines height

        args:
            value: height

        raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
