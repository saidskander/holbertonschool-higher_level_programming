#!/usr/bin/python3
"""base import"""
from models.base import Base


class Rectangle(Base):
    """class rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """self width"""
        self.__width = widht
        return self.__width

    @width.setter
    def width(self, value):
        """self setter width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not type(height) is int:
            raise TypeError('height must be an integer')
        elif type(height) is int:
            if height <= 0:
                raise ValueError('height must be > 0')
        elif type(height) is int and height > 0:
            self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not type(x) is int:
            raise TypeError("x must be an integer")
        elif type(x) is int:
            if x < 0:
                raise ValueError("x must be >= 0")
        elif type(x) is int and x > 0:
            self.x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not type(y) is int:
            raise TypeError("y must be an integer")
        elif type(y) is int:
            if y < 0:
                raise ValueError('y must be >= 0')
        elif type(y) is int and y > 0:
            self.__y = y
