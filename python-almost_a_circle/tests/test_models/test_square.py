import unittest
from models.square import Square
from models.base import Base
from unittest.mock import patch
from io import StringIO

class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_creation(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_string(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_negative_numbers(self):
        with self.assertRaises(ValueError):
            s1 = Square(-1)
        with self.assertRaises(ValueError):
            s2 = Square(1, -2)
        with self.assertRaises(ValueError):
            s3 = Square(1, 2, -3)

    def test_square_zero_values(self):
        with self.assertRaises(ValueError):
            s1 = Square(0)
        with self.assertRaises(ValueError):
            s2 = Square(1, 0)

    def test_area_method_exists(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_str_method_exist(self):
        s1 = Square(1, 2, 3)
        self.assertEqual(s1.__str__(), '[Square] (1) 2/3 - 1')

    def test_display_without_xy(self):
        """Test display method of Square without x and y"""
        s = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_xy(self):
        """Test display method of Square with x and y"""
        s = Square(2, 1, 1)
        expected_output = "\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
