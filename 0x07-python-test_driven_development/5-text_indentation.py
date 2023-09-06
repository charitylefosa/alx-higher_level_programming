#!/usr/bin/python3
"""Module composed of a function that prints 2 \
   new lines after ".?:" characters"""


def text_indentation(text):
    """Function prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Raise:
        TypeError: if text is not a string

    Return:
        No return
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d
    print(s[:-3], end="")
