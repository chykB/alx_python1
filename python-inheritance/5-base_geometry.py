#!/usr/bin/python3
"""a base moduleclass"""


class BaseGeometry:
    """a method that calculates the area but will notbe implemented"""

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
                raise ValueError("{} must be greater than 0".format(value))
            else:
                self.value = value
        else:
            raise TypeError("{} must be an integer".format(name))
