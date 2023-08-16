#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.
    attributes: width and height.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes instances width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        return width if setter doesn't raise an error.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        return height if setter doesn't raise an error.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Area of a rectangle from width and height return values.
        """
        return (self.width * self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with a larger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_2.area() >= rect_1.area():
            return (rect_2)
        return (rect_1)

    def perimeter(self):
        """
        Perimeter of a rectangle from width and height retrun values.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.width + self.height) * 2)

    @classmethod
    def square(cls, size=0):
        """
        returns new rectangle that has:
        width == height == size
        """
        return (cls(size, size))

    def __str__(self):
        """
        Returns printable string of Rectangle. By
        representation with the # symbol.
        """
        if self.width == 0 or self.height == 0:
            return ("")
        width = "#" * self.width
        rectangle = width
        for i in range(self.height - 1):
            rectangle += "\n" + width
        return (rectangle)

    def __repr__(self):
        """
        Returns a string representation of Rectangle.
        """
        rect_repr = "Rectangle({:d}, {:d})".format(self.width, self.height)
        return rect_repr

    def __del__(self):
        """
        Prints a message for every instance of rectangle deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
