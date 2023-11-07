#!/usr/bin/python3
""" BaseGeometry class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        """ init """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area function """
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
