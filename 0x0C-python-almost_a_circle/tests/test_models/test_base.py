#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
'''
from shutil import rmtree
'''


class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_base_instance(self):
        b1 = Base()
        self.assertIsInstance(b1, Base)

    def test_base_no_id(self):
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)

    def test_base_with_id(self):
        b4 = Base(6)
        self.assertEqual(b4.id, 6)

    def test_to_and_from_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        empty_dictionary = Base.to_json_string([])
        none_dictionary = Base.to_json_string(None)

        self.assertIsInstance(json_dictionary, str)
        self.assertIsInstance(empty_dictionary, str)
        self.assertEqual(empty_dictionary, "[]")
        self.assertEqual(none_dictionary, "[]")
        r1_list = Base.from_json_string(json_dictionary)
        self.assertIsInstance(r1_list, list)
        self.assertEqual(r1_list[0]['width'], dictionary['width'])
        self.assertEqual(r1_list[0]['height'], dictionary['height'])
        self.assertEqual(r1_list[0]['x'], dictionary['x'])
        self.assertEqual(r1_list[0]['y'], dictionary['y'])
        self.assertEqual(r1_list[0]['id'], dictionary['id'])

        s1 = Square(6, 6, 6)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        empty_dictionary = Base.to_json_string([])
        none_dictionary = Base.to_json_string(None)

        self.assertIsInstance(json_dictionary, str)
        self.assertIsInstance(empty_dictionary, str)
        self.assertEqual(empty_dictionary, "[]")
        self.assertEqual(none_dictionary, "[]")
        s1_list = Base.from_json_string(json_dictionary)
        self.assertIsInstance(s1_list, list)
        self.assertEqual(s1_list[0]['size'], dictionary['size'])
        self.assertEqual(s1_list[0]['x'], dictionary['x'])
        self.assertEqual(s1_list[0]['y'], dictionary['y'])
        self.assertEqual(s1_list[0]['id'], dictionary['id'])

    def test_create_instances(self):
        r2 = Rectangle(3, 5, 1)
        r2_dictionary = r2.to_dictionary()
        r3 = Rectangle.create(**r2_dictionary)
        da_string = r3.__str__()
        self.assertEqual(da_string, '[Rectangle] (1) 1/0 - 3/5')
        self.assertEqual(r2 is r3, False)
        self.assertEqual(r2 == r3, False)

        s2 = Square(3, 10, 1)
        s2_dictionary = s2.to_dictionary()
        s3 = Square.create(**s2_dictionary)
        da_string = s3.__str__()
        self.assertEqual(da_string, '[Square] (3) 10/1 - 3')
        self.assertEqual(s2 is s3, False)
        self.assertEqual(s2 == s3, False)

    def test_load_and_save_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        """
        os.chdir("tests")
        os.mkdir("unit_tests")
        os.chdir("unit_tests")
        """

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertIsInstance(list_rectangles_output, list)
        self.assertIsInstance(list_rectangles_input, list)

        for index in range(len(list_rectangles_input)):
            str_input = list_rectangles_input[index].__str__()
            str_output = list_rectangles_output[index].__str__()
            str_input_id = id(list_rectangles_input[index])
            str_output_id = id(list_rectangles_output[index])
            self.assertEqual(str_input, str_output)
            self.assertNotEqual(str_input_id, str_output_id)

        empty_list_output = Square.load_from_file()

        os.remove("Rectangle.json")
        """
        os.chdir("..")
        os.rmdir("unit_tests")
        os.chdir("..")
        """

    def test_save_and_load_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertIsInstance(list_rectangles_output, list)
        self.assertIsInstance(list_rectangles_input, list)

        for index in range(len(list_rectangles_input)):
            str_input = list_rectangles_input[index].__str__()
            str_output = list_rectangles_output[index].__str__()
            str_input_id = id(list_rectangles_input[index])
            str_output_id = id(list_rectangles_output[index])
            self.assertEqual(str_input, str_output)
            self.assertNotEqual(str_input_id, str_output_id)

        empty_list_output = Square.load_from_file()

        os.remove("Rectangle.csv")


if __name__ == '__main__':
    unittest.main()
