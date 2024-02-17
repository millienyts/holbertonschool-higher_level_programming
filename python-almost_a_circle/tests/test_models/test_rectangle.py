import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
from io import StringIO

class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_creation(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_string(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_five_arguments(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_rectangle_negative_numbers(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, 3, -4)

    def test_rectangle_zero_values(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, 0)

    def test_area_method_exists(self):
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)

    def test_str_method_exist(self):
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 3/4 - 1/2')

    def test_display_without_xy(self):
        """Test display method of Rectangle without x and y"""
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_xy(self):
        """Test display method of Rectangle with x and y"""
        r = Rectangle(2, 3, 1, 1)
        expected_output = "\n ##\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
