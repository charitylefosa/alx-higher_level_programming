#!/usr/bin/python3
""" removes all characters c and C from a string """


def no_c(my_string):
    remove1 = 'c'
    remove2 = 'C'
    new_string = ''.join([char for char in my_string if char != remove1 and
                         char != remove2])
    return new_string
