#!/usr/bin/python3
"""a class module BaseGeometry"""


class BaseGeometry:
    """a method that the area but it is not implemented"""


    def __dir__(cls) -> None:
        """list all attribute except the __init_subclass__"""
        attributes = super().__dir__()
        dir_to_return = []
        for attribute in attributes:
            if attribute != "__init_subclass__":
                dir_to_return.append(attribute)
        return dir_to_return
