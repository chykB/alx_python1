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
            if type(value) is int:
                if value < 0:
                    raise ValueError("width must be > 0")
                else:
                    self.__width = value
            else:
                raise TypeError("width must be an integer")

        @property
        def height(self):
            """the getter method"""
            return self.__height

        @height.setter
        def height(self, value):
            """the setter method"""
            if type(value) is int:
                if value < 0:
                    raise ValueError("height must be > 0")
                else:
                    self.__width = value
            else:
                raise TypeError("height must be an integer")

        @property
        def x(self):
            """the getter method"""
            return self.__x
            
        @x.setter
        def x(self, value):
            """the setter method"""
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value


        @property
        def y(self):
            """the getter method"""
            return self.__y
            
        @y.setter
        def y(self, value):
            """the setter method"""
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

