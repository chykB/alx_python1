#!/usr/bin/python3
"""the module Base"""

class Base:
    """
    this base class is the super class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """the object constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

class Rectangle(Base):
    """the Rectangle class inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle  class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        
        @property
        def width(self):
            """the getter method"""
            return self.__width

        @width.setter
        def width(self, value):
            """the setter method"""
            self.__width = value

        @property
        def height(self):
            """the getter method"""
            return self.__height

        @height.setter
        def height(self, value):
            """the setter method"""
            self.__height = value

        @property
        def x(self):
            """the getter method"""
            return self.__x
            
        @x.setter
        def x(self, value):
            """the setter method"""
            self.__x = value


        @property
        def y(self):
            """the getter method"""
            return self.__y
            
        @y.setter
        def y(self, value):
            """the setter method"""
            self.__y = value

