#!/usr/bin/python3
from 5-base_geometry import BaseGeometry

"""a subclass Rectangle"""
class Rectangle(BaseGeometry):
    """excluding the dir subclass from the dir list"""
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != "__init_subclass__"]


    """Instantiation with width and height"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
