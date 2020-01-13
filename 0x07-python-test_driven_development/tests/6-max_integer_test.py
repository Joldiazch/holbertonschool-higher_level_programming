#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def list_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
