#!/usr/bin/python3
"""
This module contains the class "Square"
that inherits from Base.
"""

from models.rectangle imports Rectangle


class Square(Rectangle):
    """object class 'square'."""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] {} {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update class attribute"""
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of square"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
