#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
Rectangle = __import__('9-rectangle').Rectangle

class TestRectangle(unittest.TestCase):

    def test_max(self):
        my_rectangle = Rectangle(4, 8)
        self.assertEqual()

"""     def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_max_int(self):
        self.assertEqual(max_integer([1, 3, 333333333]), 333333333)

    def test_float(self):
        self.assertNotEqual(max_integer([4.2, 3, 5]), 4.2)

    def test_error(self):
        with self.assertRaises(TypeError):
            self.assertRaises(max_integer(10))

    def test_neg(self):
        self.assertNotEqual(max_integer([2, 3, -5]), -5)

    def test_is_not_max(self):
        self.assertIsNot(max_integer([1, 4, 5]), 4) """
