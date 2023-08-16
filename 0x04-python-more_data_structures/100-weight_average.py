#!/usr/bin/python3
def weight_average(my_list=[]):
    """ returns the weighted average of all integers tuple """
    if not my_list:
        return 0
    ave = 0
    div = 0
    for num in my_list:
        ave += num[0] * num[1]
        div += num[1]
    return float(ave / div)
