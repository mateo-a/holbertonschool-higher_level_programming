#!/usr/bin/python3

from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys
import io


class TestRectangle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(cls):
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        r1 = Rectangle(1, 1)
        self.assertIsInstance(r1, Base)

    def test_rect_id(self):
        r3 = Rectangle(2, 3, 1, 1, 100)
        self.assertEqual(r3.id, 100)

    def test_rect_height_width(self):
        r4 = Rectangle(3, 3)
        self.assertEqual(r4.width, 3)
        self.assertEqual(r4.height, 3)

    def test_rect_x_y(self):
        r5 = Rectangle(5, 5, 5, 5)
        self.assertEqual(r5.x, 5)
        self.assertEqual(r5.y, 5)
        r6 = Rectangle(1, 1, 0, 0)
        self.assertEqual(r6.x, 0)
        self.assertEqual(r6.y, 0)

    def test_rect_valid_type(self):
        self.assertRaises(TypeError, Rectangle, "string", 1)
        self.assertRaises(TypeError, Rectangle, 1, "string")
        self.assertRaises(TypeError, Rectangle, [1], 1)
        self.assertRaises(TypeError, Rectangle, 1, (1,))
        self.assertRaises(TypeError, Rectangle, 1, 1.1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1.1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, 1.1)
        self.assertRaises(TypeError, Rectangle, 1, 1, (1,), 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, (1,))

    def test_rect_valid_value(self):
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaises(ValueError, Rectangle, 1, -100)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaises(ValueError, Rectangle, 1, 1, -1, 1)
        self.assertRaises(ValueError, Rectangle, 1, 1, 1, -2)

    def test_area(self):
        r7 = Rectangle(2, 6)
        self.assertEqual(r7.area(), 12)

    def test_display(self):
        sys.stdout = io.StringIO()
        r8 = Rectangle(3, 3)
        r8.display()
        self.assertEqual(sys.stdout.getvalue(), "###\n###\n###\n")

    def test_str(self):
        r9 = Rectangle(9, 9)
        da_string = r9.__str__()
        self.assertEqual(da_string, '[Rectangle] (1) 0/0 - 9/9')

    def test_display_with_coordinate(self):
        sys.stdout = io.StringIO()
        r10 = Rectangle(2, 2, 2, 2)
        r10.display()
        self.assertEqual(sys.stdout.getvalue(), "\n\n  ##\n  ##\n")

    def test_update_args(self):
        r11 = Rectangle(10, 10, 10, 10)
        r11.update(89, 2, 3, 4, 5)
        self.assertEqual(r11.id, 89)
        self.assertEqual(r11.width, 2)
        self.assertEqual(r11.height, 3)
        self.assertEqual(r11.x, 4)
        self.assertEqual(r11.y, 5)
        self.assertRaises(TypeError, r11.update, 89, "str")
        self.assertRaises(ValueError, r11.update, 89, -1, 1)
        self.assertRaises(ValueError, r11.update, 89, 1, 1, -1)
        self.assertRaises(ValueError, r11.update, 89, 1, 1, -1, -1)

    def test_update_kwarg(self):
        r12 = Rectangle(11, 11, 11, 11)
        r12.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r12.x, 1)
        self.assertEqual(r12.y, 3)
        self.assertEqual(r12.height, 2)
        self.assertEqual(r12.width, 4)
        self.assertRaises(TypeError, r12.update, x='str')
        self.assertRaises(TypeError, r12.update, y=[1])
        self.assertRaises(TypeError, r12.update, height=(1,))
        self.assertRaises(TypeError, r12.update, width=3.4)
        self.assertRaises(ValueError, r12.update, x=-1)
        self.assertRaises(ValueError, r12.update, y=-1)
        self.assertRaises(ValueError, r12.update, height=-1)
        self.assertRaises(ValueError, r12.update, width=-1)

    def test_to_dictionary(self):
        r13 = Rectangle(10, 2, 1, 9)
        r13_dictionary = r13.to_dictionary()
        test_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(r13_dictionary, test_dictionary)


if __name__ == '__main__':
    unittest.main()
