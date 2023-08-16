#!/usr/bin/python3
"""Unittest for Rectangle"""

import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """object or variable set uu for test"""
        self.rectangle = Rectangle(5, 10)

    def tearDown(self):
        """resources clean up used for test"""
        self.rectangle = None

    def test_height_getter(self):
        """test for height getter method"""
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.height, 10)

    def test_height_setter(self):
        """test for height setter method"""
        rectangle = Rectangle(5, 10)
        rectangle.height = 12
        self.assertEqual(rectangle.height, 12)

    def test_x_getter(self):
        """test for x getter method"""
        rectangle = Rectangle(5, 10, 2, 3)
        self.assertEqual(rectangle.x, 2)

    def test_x_setter(self):
        """test for x setter method"""
        rectangle = Rectangle(5, 10, 2, 3)
        rectangle.x = 4
        self.assertEqual(rectangle.x, 4)

    def test_y_getter(self):
        """test for y getter method"""
        rectangle = Rectangle(5, 10, 2, 3)
        self.assertEqual(rectangle.y, 3)

    def test_y_setter(self):
        """test for y setter method"""
        rectangle = Rectangle(5, 10, 2, 3)
        rectangle.y = 5
        self.assertEqual(rectangle.y, 5)

    def test_update_args(self):
        """test for args method"""
        rectangle = Rectangle(5, 10)
        rectangle.update(2, 8, 12, 3, 4)
        expd_dict = {'id': 2, 'width': 8, 'height': 12, 'x': 3, 'y': 4}
        self.assertEqual(rectangle.to_dictionary(), expd_dict)

    def test_width_setter_type_error(self):
        """test for width setter TypeError"""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(TypeError):
            rectangle.width = 3.14

    def test_width_setter_value_error(self):
        """test for width setter ValueError"""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rectangle.width = -5

    def test_height_setter_type_error(self):
        """test for height setter TypeError"""
        rectangle = Rectangle(5, 10)
        rectangle.height = True

    def test_height_setter_value_error(self):
        """ test for height setter ValueError"""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rectangle.height = -10

    def test_x_setter_type_error(self):
        """test for x setter TypeError"""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(TypeError):
            rectangle.x = [1, 2, 3]

    def test_x_setter_value_error(self):
        """test for x setter ValueError"""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rectangle.x = -2

    def test_y_setter_type_error(self):
        """test for y setter TypeError"""
        rectangle = Rectangle(5, 10, 2, 3)
        with self.assertRaises(TypeError):
            rectangle.y = {"y": "3"}

    def test_y_setter_value_error(self):
        """test for y setter ValueError"""
        rectangle = Rectangle(5, 10 2, 3)
        with self.assertRaises(ValueError):
            rectangle.y = -3


if __name__ == '__main__':
    unittest.main()
