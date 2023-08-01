#!/usr/bin/python3
"""a class module BaseGeometry"""


class BaseGeometry:
    """this is an empty class"""
    pass
    
    def __dir__(cls) -> None:
        """listt all attribute of this class exclude the __init__subclass"""
        attributes = super().__dir__()
        return [attribute for attribute is attributes if attribute != "__init__subclass"]
