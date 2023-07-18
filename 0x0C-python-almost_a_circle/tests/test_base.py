#!/usr/bin/python3

"""
    Unittests for Base module
"""

import unittest
import os
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for Base class
    """

    def test_creation_id(self):
        """
        Test if the value of id is assigned correctly
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(42)
        b5 = Base(-17)
        b6 = Base(3.14)
        b7 = Base()
        b8 = Base(None)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 42)
        self.assertEqual(b5.id, -17)
        self.assertEqual(b6.id, 3.14)
        self.assertEqual(b7.id, 4)
        self.assertEqual(b8.id, 5)

    def test_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_from_json_string(self):
        json_string = Base.from_json_string(None)
        self.assertEqual(json_string, [])

    def test_base_conformance(self):
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_rectangle_conformance(self):
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_square_conformance(self):
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0)

    def test_create_rectangle(self):
        r1 = Rectangle(4, 5, 10)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        s1 = Square(3, 8, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

    def test_id_int(self):
        b = Base(20)
        self.assertEqual(b.id, 20)
        b = Base(0)
        self.assertEqual(b.id, 0)
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_incrementation(self):
        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(7)
        self.assertEqual(b.id, 7)
        b = Base(None)
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)

    def test_id_non_int(self):
        b = Base("Hello")
        self.assertEqual(b.id, "Hello")
        b = Base('A')
        self.assertEqual(b.id, 'A')
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])
        b = Base((1, 2))
        self.assertEqual(b.id, (1, 2))
        b = Base({"id": 7, "name": "Henry"})
        self.assertEqual(b.id, {"id": 7, "name": "Henry"})
        b = Base(False)
        self.assertEqual(b.id, False)

    def test_id_error(self):
        with self.assertRaises(TypeError):
            b = Base(1, 2)
        with self.assertRaises(TypeError):
            b = Base(1, None)

    def test_rectangle_to_json_string(self):
        r = Rectangle(8, 6, 2, 4, 10)
        r_dict = r.to_dictionary()
        json_string = Base.to_json_string([r_dict])
        self.assertEqual(str, type(json_string))

    def test_rectangle_from_json_string(self):
        json_string = '[{"id": 1, "width": 8, "height": 6, "x": 2, "y": 4}]'
        result = Base.from_json_string(json_string)
        self.assertEqual(list, type(result))
        self.assertEqual(1, len(result))
        self.assertEqual(dict, type(result[0]))

    def test_square_to_json_string(self):
        s = Square(5, 2, 4, 10)
        s_dict = s.to_dictionary()
        json_string = Base.to_json_string([s_dict])
        self.assertEqual(str, type(json_string))

    def test_square_from_json_string(self):
        json_string = '[{"id": 1, "size": 5, "x": 2, "y": 4}]'
        result = Base.from_json_string(json_string)
        self.assertEqual(list, type(result))
        self.assertEqual(1, len(result))
        self.assertEqual(dict, type(result[0]))

    def test_save_one_rectangle(self):
        r = Rectangle(8, 6, 2, 4, 10)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 53)

    def test_save_two_rectangles(self):
        r1 = Rectangle(8, 6, 2, 4, 10)
        r2 = Rectangle(4, 2, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

    def test_save_one_square(self):
        s = Square(5, 2, 4, 10)
        Square.save_to_file([s])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 39)

    def test_save_two_squares(self):
        s1 = Square(5, 2, 4, 10)
        s2 = Square(4, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 77)

    def test_save_overwrite(self):
        s = Square(4, 3, 2, 1)
        Square.save_to_file([s])
        s = Square(5, 2, 4, 10)
        Square.save_to_file([s])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 39)

    def test_save_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_two_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


if __name__ == '__main__':
    unittest.main()
