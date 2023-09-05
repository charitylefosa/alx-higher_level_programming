#!/usr/bin/python3
def magic_string(s=[0]):
    s[0] += 1
    return str("BestSchool, " * (s[0] - 1)) + "BestSchool"
