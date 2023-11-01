#!/usr/bin/python3
"""
    a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ prints a text with 2 new lines if it's ends with . , ? and : """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip().replace(". ", ".\n\n")\
                       .replace("? ", "?\n\n")\
                       .replace(": ", ":\n\n")

    print(text, end="")
