#!/usr/bin/python3
""" 2. First Rectangle """
from models.base import Base


class Rectangle (Base):
    """ Defines a Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle object """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area value """
        return self.width * self.height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for y in range(self.y):
            print('')
        for row in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for col in range(self.width):
                print('#', end='')
            print('')

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}'

    def update(self, *args):
        """
        assigns an argument to each attribute

        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        try:
            print(args)
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
