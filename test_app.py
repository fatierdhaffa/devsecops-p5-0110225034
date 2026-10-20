
import unittest

from app import calculate
from calculator import add, subtract, multiply, divide
from validator import validate_number
from formatter import format_result
from security_utils import validate_operation


class TestSecureCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            validate_number("abc")

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            validate_operation("%")

    def test_calculate(self):
        self.assertEqual(calculate(10, "+", 5), 15)

    def test_format_result(self):
        self.assertEqual(format_result(5.0), "5")


if __name__ == "__main__":
    unittest.main()
