#!/usr/bin/python3

import unittest
from models.base import Base
from models import Rectangle
from models.rectangle import Rectangle
Rectangle = Rectangle


class TestRectangle(unittest.TestCase):
    def test_getter_setter(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(5, 2)
        self.assertEqual(r1.id, 1)


if __name__ == '__main__':
    unittest.main()
