#!/usr/bin/python3

import sys

if __name__ == "__main__":
    count = len(sys.argv) - 1
    if count == 0:
         print("0 arguments.")
    elif count == 1:
         print("1 arguments.")
    else:
        print("{} argument:".format(count))
    for number in range(count):
        print("{}: {}".format(number + 1, sys.argv[number + 1]))