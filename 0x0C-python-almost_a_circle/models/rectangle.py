#!/usr/bin/python3
""" class Rectangle base inherit """
from models.base import Base


class Rectangle(Base):
    """ class a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle """
        self.width = width
        self.height = height
        super().__init__(id)
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter_height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter x """
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter of y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return an area class """
        return (self.height * self.width)

    def display(self):
        """ Display (#) of the class """
        for y in range(self.y):
            print()
        for l in range(self.height):
            for x in range(self.x):
                print(end=" ")
            for o in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ print string """
        string = (
                "[Rectangle] (" + str(self.id) +
                ") " +
                str(self.x) + "/" +
                str(self.y) + " - " +
                str(self.width) +
                "/" +
                str(self.height)
                )
        return (string)

    def update(self, *args, **kwargs):
        """ update with args and kwargs """
        if args:
            i = ['id', 'height', 'width', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, i[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary """
        dict = dict()
        dict['id'] = self.id
        dict['height'] = self.height
        dict['width'] = self.width
        dict['y'] = self.y
        dict['x'] = self.x
        return dict
