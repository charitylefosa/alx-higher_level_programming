#!/usr/bin/python3
"""composed od class Student"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary rep of student instance"""
        return self.__dict__
