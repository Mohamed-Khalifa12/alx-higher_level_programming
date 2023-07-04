#!/usr/bin/python3
"""1 - rectangle with width and hight"""


class Rectangle:
    """define width and hight"""

    def __init__(self, width=0, height=0):
        """instantiation of the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width with error detection"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """"get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height with error detection"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
