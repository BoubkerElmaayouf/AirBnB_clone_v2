#!/usr/bin/python3
""" Module document"""
import unittest
import console


class test_Console(unittest.TestCase):
    """doc document"""

    def test_documentation(self):
        """doc document"""
        self.assertIsNotNone(console.__doc__)