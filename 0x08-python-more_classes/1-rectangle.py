#!/usr/bin/python3
# 1-rectangle.py
# Hammad-Ibrahim <hammad-ibrahim@alxschool.com > 
""" define a Rectangle Class """


class rectangle:
    """ Represent a Rectangle """ 
    def __init__ (self, width=0, hight=0):
        """ Initialize a new Rectangle 

        args:
            width (int) = the width of a new rectangle 
            hight (int) = the hight of a new rectangle
        """
        self.width = width 
        self.hight = hight


    @property
    def width(self):
        """ Get/set the Width of a rectangle """
        return self.__width


    @width.setter
    def width(self, value):
        if not isinstance (value, int):
            raise TypeError ("Width Must be an integer ")
        if value <  0:
            raise TypeError ("width Must be >=0 ")
        slef.__width = value


    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    


