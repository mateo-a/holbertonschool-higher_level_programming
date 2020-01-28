#!/usr/bin/python3
import unittest
import pep8


class TestBase(unittest.TestCase):
    """Test clase"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8check = pep8.StyleGuide(quiet=True)
        result = pep8check.check_files(['models/base.py', 'models/square.py', 'models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
