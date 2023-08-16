#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """2 C functions that print basic info on Python lists & bytes objects """
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
        return a_dictionary
