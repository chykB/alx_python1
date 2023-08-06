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
        def width(self):
            """the getter method"""
            self.__height = height

        @width.setter
        def width(self, height):
            """the setter method"""
            self.__height = height

        @property
        def width(self):
            """the getter method"""
            self.__x = x
            
        @width.setter
        def width(self, x):
            """the setter method"""
            self.__x = x


        @property
        def width(self):
            """the getter method"""
            self.__y = y
            
        @width.setter
        def width(self, y):
            """the setter method"""
            self.__y = y

