#!/usr/bin/python3



"""return if the object is an instance of a class that inherited from a class"""
def inherits_from(obj, a_class):
    """the return statement"""
    if not isinstance(a_class, type) or not isinstance(obj, type):
        pass
    return issubclass(type(obj), a_class)
