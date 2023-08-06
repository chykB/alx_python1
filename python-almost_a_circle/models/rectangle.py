#!/usr/bin/python3
"""the module Base"""
from models.base import Base
"""the rectangle module"""


class Rectangle(Base):
    """The Rectangle class inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """The getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter method for width"""
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """The getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter method for height"""
        if type(value) is int:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """The getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter method for x"""
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """The getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The setter method for y"""
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
