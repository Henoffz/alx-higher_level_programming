#!/usr/bin/python3
"""Test for Square"""

from models.square import Square
import unittest
from models.rectangle import Rectangle
from models.base import Base
import os
from contextlib import redirect_stdout
import json


class TestSquare(unittest.TestCase):
    def setUp(self):
        """object set up for test"""
        self.square = Square(5)

    def tearDown(self):
        """clean up test resources"""
        self.square = None

    def test_size_getter(self):
        """test for size getter method"""
        self.assertEqual(self.square.size, 5)

    def test_size_setter(self):
        """test for size setter method"""
        self.square.size = 8
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.width, 8)
        self.assertEqual(self.square.height, 8)

    def test_update_args(self):
        """test for args update method"""
        self.square.update(2, 8, 3, 4)
        expected_dict = {'id': 2, 'size': 8, 'x': 3, 'y': 4}
        self.assertEqual(self.square.to_dictionary(), expected_dict)

    def test_to_dictionary(self):
        """test for dictionary"""
        expected_dict = {'id': 1, 'size': 5, 'x': 0, 'y': 0}
        self.assertEqual(self.square.to_dictionary(), expected_dict)

    def test_size_setter_type_error(self):
        """TypeError test for size setter method"""
        with self.assertRaises(TypeError):
            self.square.size = 2.33

    def test_size_setter_value_error(self):
        """ValueError test for size setter method"""
        with self.assertRaises(ValueError):
            self.square.size = -8

    def test_size_setter_type_error(self):
        """TypeError test for size setter method"""
        with self.assertRaises(TypeError):
            self.square.size = "hello"

    def test_size_setter_type_error(self):
        """TypeError test for size setter method"""
        with self.assertRaises(TypeError):
            self.square.size = None

    def test_update_args_type_error(self):
        """TypError test for update args method"""
        with self.assertRaises(TypeError):
            self.square.update(2, "abc", 3, 4)

    def test_update_args_value_error(self):
        """ValueError test for args update method"""
        with self.assertRaises(ValueError):
            self.square.update(2, -8, 3, 4)

    def test_update_kwargs_type_error(self):
        """TypeError test for kwargs update method"""
        with self.assertRaises(TypeError):
            self.square.update(id=2, size="xyz", x=3, y=4)

    def test_update_kwargs_value_error(self):
        """ValueError test for kwargs update method"""
        with self.assertRaises(ValueError):
            self.square.update(id=2, size=-8, x=3, y=4)


if __name__ == '__main__':
    unittest.main()
