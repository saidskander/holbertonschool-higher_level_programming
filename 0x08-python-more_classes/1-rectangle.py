#!/usr/bin/python3
"""ectangle-c-lass"""


class Rectangle:
    """rectangle"""

    def __init__(self, width=0, height=0):
        """sef init"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    def width(self):
        """self-getter"""
        return self.__width

    def width(self, value):
        """self-setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def height(self):
        """self-getter"""
        return self.__height

    def height(self, value):
        """self-setter"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
