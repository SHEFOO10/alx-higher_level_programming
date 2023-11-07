#!/usr/bin/python3
""" 0. Read file """


def read_file(filename=""):
    """
        reads a text file (UTF8) and prints it to stdout.

        Args:
            filename (str): filename.
    """
    with open(filename, encoding='UTF8') as f:
        print(f.read(), end='')
