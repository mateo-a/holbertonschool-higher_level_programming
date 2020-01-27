#!/usr/bin/python3
"""Test for Square Module"""


from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import unittest
import sys
import io


class TestSquare(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(cls):
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        s1 = Square(3)
        self.assertIsInstance(s1, Rectangle)

    def test_square_id(self):
        s3 = Square(2)
        self.assertEqual(s3.id, 1)

    def test_square_height_width(self):
        s4 = Square(3)
        self.assertEqual(s4.width, 3)
        self.assertEqual(s4.height, 3)

    def test_square_x_y(self):
        s5 = Square(5, 1, 1)
        self.assertEqual(s5.x, 1)
        self.assertEqual(s5.y, 1)
        s6 = Square(1, 2, 3)
        self.assertEqual(s6.x, 2)
        self.assertEqual(s6.y, 3)

    def test_square_valid_type(self):
        self.assertRaises(TypeError, Square, "string", 1)
        self.assertRaises(TypeError, Square, 1, "string")
        self.assertRaises(TypeError, Square, [1], 1)
        self.assertRaises(TypeError, Square, 1, (1,))
        self.assertRaises(TypeError, Square, 1, 1.1)
        self.assertRaises(TypeError, Square, 1, 1, 1.1)

    def test_square_valid_value(self):
        self.assertRaises(ValueError, Square, -1, 1)
        self.assertRaises(ValueError, Square, 1, -100)
        self.assertRaises(ValueError, Square, 0, 1)
        self.assertRaises(ValueError, Square, -1, 1)
        self.assertRaises(ValueError, Square, 1, 1, -1, 1)

    def test_area(self):
        s7 = Square(2)
        self.assertEqual(s7.area(), 4)

    def test_display(self):
        sys.stdout = io.StringIO()
        s8 = Square(3)
        s8.display()
        self.assertEqual(sys.stdout.getvalue(), "###\n###\n###\n")

    def test_str(self):
        s9 = Square(9)
        da_string = s9.__str__()
        self.assertEqual(da_string, '[Square] (1) 0/0 - 9')

    def test_display_with_coordinate(self):
        sys.stdout = io.StringIO()
        s10 = Square(2, 2, 2)
        s10.display()
        self.assertEqual(sys.stdout.getvalue(), "\n\n  ##\n  ##\n")

    def test_update_args(self):
        s11 = Square(10, 10, 10, 10)
        s11.update(89, 2, 3, 4)
        self.assertEqual(s11.id, 89)
        self.assertEqual(s11.size, 2)
        self.assertEqual(s11.width, 2)
        self.assertEqual(s11.x, 3)
        self.assertEqual(s11.y, 4)
        self.assertRaises(TypeError, s11.update, 89, "str")
        self.assertRaises(TypeError, s11.update, 1, 1, "str")
        self.assertRaises(TypeError, s11.update, 1, 1, 1, "str")
        self.assertRaises(ValueError, s11.update, 89, -1, 1)
        self.assertRaises(ValueError, s11.update, 89, 1, -1)
        self.assertRaises(ValueError, s11.update, 89, 1, 1, -1)

    def test_update_kwarg(self):
        s12 = Square(11, 11, 11, 11)
        s12.update(x=1, y=3, size=2)
        self.assertEqual(s12.id, 11)
        self.assertEqual(s12.x, 1)
        self.assertEqual(s12.y, 3)
        self.assertEqual(s12.size, 2)
        self.assertRaises(TypeError, s12.update, x='str')
        self.assertRaises(TypeError, s12.update, y=[1])
        self.assertRaises(TypeError, s12.update, size=3.4)
        self.assertRaises(ValueError, s12.update, x=-1)
        self.assertRaises(ValueError, s12.update, y=-1)
        self.assertRaises(ValueError, s12.update, size=-1)

    def test_to_dictionary(self):
        s13 = Square(10, 2, 1)
        s13_dictionary = s13.to_dictionary()
        test_dictionary = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(s13_dictionary, test_dictionary)


if __name__ == '__main__':
    unittest.main()
