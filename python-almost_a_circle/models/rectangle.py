#!/usr/bin/python3
"""importing from the Base class"""
from models.Base import Base
"""a rectangle that inherits from the module Base"""

class Rectangle(Base):
    """the Rectangle classinerits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle  class constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
        
        @property
        def width(self):
            """the getter method"""
            self.__width = width

        @width.setter
        def width(self, width):
            """the setter method"""
            self.__width = width

        @property
        def height(self):
            """the getter method"""
            self.__height = height

        @height.setter
        def height(self, height):
            """the setter method"""
            self.__height = height

        @property
        def x(self):
            """the getter method"""
            self.__x = x
            
        @x.setter
        def x(self, x):
            """the setter method"""
            self.__x = x


        @property
        def y(self):
            """the getter method"""
            self.__y = y
            
        @y.setter
        def y(self, y):
            """the setter method"""
            self.__y = y

