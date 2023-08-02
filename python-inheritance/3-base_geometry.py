#!/usr/bin/python3

"""a class module BaseGeometry"""
class BaseGeometry:
    """this is an empty class"""
    
     def __dir__(cls) -> None:
        """
           list all attribute except the __init_subclass__
        """
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != "__init_subclass__"]
