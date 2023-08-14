#!/usr/bin/python3
def multiple_returns(sentence):
    """ returns a tuple with the length of a string and its first character."""
    if len(sentence) == 0:
        f_char = None
    else:
        f_char = sentence[0]
    result = (len(sentence), f_char)
    return result
