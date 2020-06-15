#!/usr/bin/python3
"""Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def __str__(self):
        """String square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}"
                                    .format(self.id, self.x,
                                        self.y, self.width)

    def update(self, *args, **kwargs):
        """update"""
        if len(args):
            for x, l in enumerate(args):
                if x == 0:
                    self.id = l
                elif x == 1:
                    self.size = l
                elif x == 2:
                    self.x = l
                elif x == 3:
                    self.y = l
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "x" in kwargs:
                self.x = kwargs["x"]

    def to_dictionary(self):
        """dictionary square"""
        m = {}
        m["id"] = self.id
        m["size"] = self.size
        m["y"] = self.y
        m["x"] = self.x
        return m
