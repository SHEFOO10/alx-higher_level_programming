#!/usr/bin/python3
""" returns the list of available attributes """


def lookup(obj):
    """
        a function that returns the list of available attributes
            and methods of an object
    """
    return dir(obj)
