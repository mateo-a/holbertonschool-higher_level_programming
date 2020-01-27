#!/usr/bin/python3


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base"""
    def setUp(self):
        """Setup for each test"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test id"""
        b = Base(7)
        self.assertEqual(b.id, 7)

    def no_test_id(self):
        """No id received"""
        b = Base()
        self.assertEqual(1, b.id)
