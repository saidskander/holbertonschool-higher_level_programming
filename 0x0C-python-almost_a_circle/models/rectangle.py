#!/usr/bin/python3
"""base import"""
from .base import Base


class Rectangle(Base):
    """class rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """self width"""
        return self.__width

    @width.setter
    def width(self, value):
        """self setter width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
