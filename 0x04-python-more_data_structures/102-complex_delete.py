#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """2 C functions that print basic info on Python lists & bytes objects """
    key_list = list(a_dictionary.keys())
    for key in key_list:
        if value == a_dictionary.get(key):
            del a_dictionary[key]
    return a_dictionary
