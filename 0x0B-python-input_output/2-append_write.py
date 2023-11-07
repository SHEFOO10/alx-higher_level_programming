#!/usr/bin/python3
""" 2. Append to a file """


def append_write(filename="", text=""):
    """
        a function that appends a string at the end of a text file (UTF8)
        and returns the number of characters added

        Args:
            filename (str): file name.
            text (str): text.
    """
    with open(filename, 'a', encoding='UTF8') as f:
        wc = f.write(text)
    return wc
