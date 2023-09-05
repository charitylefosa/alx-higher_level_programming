#!/usr/bin/python3
""" Module composed of a class that defines a rectangle """


class Rectangle:
    """ Class defining a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method initializing the instance

        Args:
            width : rectangle width
            height : rectangle height
            number_of_instances: increment/decrement count
            print_symbol: symbol for string representation
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            rect_str.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect_str)

    def __repr__(self):
        """ returning string representation of rectangle for eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """destructor method"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Method returning the bigger rectangle

        Args:
            rect_1: rectangle 1
            rect_2: rectangle 2

        Raise:
            TypeError: when some argument pass is not an \
            instance of the rectangle class
        Return:
            bigger rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ creating new rectangle instance with width and height equal \
        to given size

        Args:
            size(int): size of square (default is 0)

        Return:
            rectangle: new rectangle instance representing a square
        """
        return cls(size, size)
