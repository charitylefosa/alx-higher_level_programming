#!/usr/bin/python3
"""New Class"""


class MyInt(int):
    """inherits form int"""
    def __eq__(self, num):
        """function for equals"""
        return (int(self) != int(num))

    def __ne__(self, num):
        """function for not equals"""
        return (int(self) == int(num))
