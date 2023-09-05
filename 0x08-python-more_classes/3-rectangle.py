#!/usr/bin/python3
""" Module composed of a class that defines a rectangle """


class Rectangle:
    """ Class defining a rectangle """

    def __init__(self, width=0, height=0):
        """ Method initializing the instance

        Args:
            width : rectangle width
            height : rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Method returning the value of the width

        Return:
            rectangle width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ Method defining width

        Args:
            value: width
        Return:
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
        """ Method returning the value of the height

        Return:
            rectangle height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ Method defining height

        Args:
            value: height
        Return:
            TypeError: if height is not an integer
            ValueError: if height is less than
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method calculating area of a rectangle

        Returns:
            area
        """
        return self.width * self.height

    def perimeter(self):
        """ Method calculating perimeter of a rectangle

        Return:
            perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """Returning string representation of rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = []
        for i in range(self.__height):
            rect_str.append("#" * self.__width)
        return "\n".join(rect_str)
