#!/usr/bin/python3
""" 1. Write to a file """


def write_file(filename="", text=""):
    """
        a function that writes a string to a text file (UTF8)
        and returns the number of characters written

        Args:
            filename (str): filename.
            text (str): text.
    """
    with open(filename, 'w', encoding='UTF8') as f:
        wc = f.write(text)
    return wc
