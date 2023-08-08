#!/usr/bin/python3
for i in range(100):
    numbs = str(i).zfill(2)
    if i != 99:
        print("{}, ".format(numbs), end="")
    else:
        print("{}".format(numbs), "\n")
