#!/usr/bin/python3
""" Define a class Square."""


class Square:
    """ Initialize a Square with specific size"""
    def __init__(self, size=0):
        """
            define a Square

            Args:
                size (int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """
            method that calculates area of the square.

            Return: Area
        """
        return self.__size ** 2
