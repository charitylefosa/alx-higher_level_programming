#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ finds all multiples of 2 in a list."""
    list2 = my_list[0]
    for num in my_list:
        if num % 2 == 0:
            return True
