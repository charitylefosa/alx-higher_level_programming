#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num_elements = 0
    for num_elements in range(x):
       try:
           print("{}".format(my_list[num_elements]), end="")
           num_elements += 1
       except Exception:
           break
    print("")
    return (num_elements)
