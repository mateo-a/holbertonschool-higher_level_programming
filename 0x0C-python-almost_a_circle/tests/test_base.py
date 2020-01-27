#!/usr/bin/python3


import unittest
from models.base import Base
Base = Base


class TestBase(unittest.TestCase):
    """Test cases for Base"""
    def test_id(self):
        """Test id"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)


if __name__ == '__main__':
    unittest.main()
