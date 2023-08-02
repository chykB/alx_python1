#!/usr/bin/python3
"""a base moduleclass"""


class BaseGeometry:
    """a method that excludes the __init_subclass__ from the dir"""
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != "__init_subclass__"]

    """a method that calculates the area but is not implemented"""
    def area(self):
        """an exception raised"""
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        self.name = "name"
        """
        value: validating the value
        """
        if type(value) is int:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
            else:
                self.value = value
        else:
            raise TypeError("{} must be an integer".format(name))

    """a subclass Rectangle"""
class Rectangle(BaseGeometry):

    """a method that excludes the __init_subclass__ from the dir"""
    def __dir__(self) -> None:
        attributes = dir(self).__dir__()
        return [attribute for attribute in attributes if attribute != "__init_subclass__"]


    """Instantiation with width and height"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    """the area of the rectangle implemented"""
    def area(self):
        return self.__width * self.__height

    """print out rectangle description"""
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

"""a subclas Square that inherits from the class Rectangle"""
class Square(BaseGeometry):
    """instantiate with size whic is private"""
    def __init__(self, size):
        super().__init__() 
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2
