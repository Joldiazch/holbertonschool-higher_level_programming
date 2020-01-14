#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def empty_list(self):
        self.assertIsNone(max_integer([]))

    def max_num(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 999e999]), 999e999)

    def negativ_number(self):
        self.assertNotEqual(max_integer[-8, -5, -3, -2, 1], -8)

    def type_error(self):
        with self.assertRaises(TypeError):
            self.assertRaises(max_integer(5))
