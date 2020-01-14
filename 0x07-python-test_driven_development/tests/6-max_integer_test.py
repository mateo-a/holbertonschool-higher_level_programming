#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for max_integer"""

    def test_max_positive_1(self):
        """Tests a list with positives"""
        self.assertEqual(max_integer([1, 2, 5, 0, 3]), 5)

    def test_max_positive_2(self):
        """Tests a list with positives"""
        self.assertEqual(max_integer([9, 2, 5, 0, 3]), 9)

    def test_max_positive_3(self):
        """Tests a list with positives"""
        self.assertEqual(max_integer([1, 2, 5, 0, 9]), 9)

    def test_max_negative(self):
        """Tests a list with a negative"""
        self.assertEqual(max_integer([-9, 2, 5, 6, 3]), 6)

    def test_max_negatives(self):
        """Tests a list with negatives numbers"""
        self.assertEqual(max_integer([-2, -8, -4, -7, -3]), -2)

    def test_max_zero(self):
        """Tests a list with 0 and negatives"""
        self.assertEqual(max_integer([-2, -8, -4, 0, -3]), 0)

    def test_max_duplicated(self):
        """Tests a list with duplicated values"""
        self.assertEqual(max_integer([-4, -8, -4, 3, 3]), 3)

    def test_max_sameval(self):
        """Tests a list with equal values"""
        self.assertEqual(max_integer([4, 4, 4, 4, 4]), 4)

    def test_max_one(self):
        """Tests a list with one value"""
        self.assertEqual(max_integer([7]), 7)

    def test_max_empty(self):
        """Tests an empty list"""
        self.assertIs(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()