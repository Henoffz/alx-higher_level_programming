#!/usr/bin/python3
"""Defines a class 'Recangle' that
inherits from parent class 'Base'."""

from models.base import Base


class Rectangle(Base):
    """subclass of a parent class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation of class."""
        super().__init__(id)
        """calls function of superclass and passes id arg"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @propery
    def height(self):
        """getter method for height atribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter method for attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for attribute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter method for attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for attribute y"""
        if type(value) is not int:
            raise TypeError("y must be an ineger")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints rectangle using # symbol"""
        print("\n" * self.__y, end="")
        print((' ' * self.x + "#" * self.width + '\n') * self.height, end="")

    def __str__(self):
        """return formatted rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute of the Rectangle"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of rectangle"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x,
                'y': self.y}
