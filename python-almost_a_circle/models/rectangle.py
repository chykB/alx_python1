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

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width


        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height


        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x


        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y



    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter method for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter method for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The setter method for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """this method calculate the area of the rectangle"""
        return self.width * self.height


    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__height):
                print("#" * self.__width)


    def __str__(self):
        """this method convert object to string"""
        return str("[Rectangle] {} {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))
