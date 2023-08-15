#!/usr/bin/python3
def max_integer(my_list=[]):
    """ finds the biggest integer of a list."""
    if my_list == []:
        return None
    value = my_list[0]
    for num in my_list:
        if num > value:
            value = num
    return value
