#!/usr/bin/python3
"""composed od class Student"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary rep of student instance"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of student"""
        for k, v in json.items():
            setattr(self, k, v)
