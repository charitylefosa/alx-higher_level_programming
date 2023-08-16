#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ adds all unique integers in a list (only once for each integer). """
    uniq = set(my_list)
    result = 0
    for i in uniq:
        result += i
    return result
