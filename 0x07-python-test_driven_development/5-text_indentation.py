#!/usr/bin/python3
"""text_indentation function"""


def text_indentation(text):
    """text_indentation function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = False
    for char in text.strip():
        if char == ' ':
            if not new_line:
                print(' ', end='')
        elif char in ".?:":
            print(char, end='\n\n')
            new_line = True
        else:
            print(char, end='')
            new_line = False
