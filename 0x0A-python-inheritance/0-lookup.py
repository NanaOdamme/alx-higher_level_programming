#!/usr/bin/python3
"""
    This module returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """Use the dir() function to get list attributes and methods of object"""
    attributes_and_methods = dir(obj)

    return attributes_and_methods
