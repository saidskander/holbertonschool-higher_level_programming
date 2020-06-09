#!/usr/bin/python3
"""
importing the Base
module from moduls
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle is class rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """self widht"""
        self.__width = width
        return self.__width

    @width.setter
    def width(self, width):
        """setter widht"""
        if not type(width) is int:
            raise TypeError("width must be an integer")
        elif type(width) is int:
            if width <= 0:
                raise ValueError("width must be > 0")
        elif type(width) is int and width > 0:
            self.__width = width
