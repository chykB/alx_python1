#!/usr/bin/python3



"""return if the object is an instance of a class that inherited from a class"""
def inherits_from(obj, a_class):
    """the return statement"""
    return isinstance(obj, a_class) and type(obj) != a_class
