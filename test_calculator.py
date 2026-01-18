"""
Unit tests for the calculator module.
"""

import unittest
from calculator import Calculator
from utils import calculate


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-3, -3), 0)

    def test_multiply(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, 2), -3)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(5, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))

    def test_power(self):
        """Test power operation."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(2, -1), 0.5)

    def test_modulo(self):
        """Test modulo operation."""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(15, 5), 0)
        self.assertEqual(self.calc.modulo(7, 4), 3)

    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.modulo(5, 0)
        self.assertIn("Cannot perform modulo with zero", str(context.exception))

    def test_square_root(self):
        """Test square root operation."""
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertEqual(self.calc.square_root(0), 0)

    def test_square_root_negative(self):
        """Test square root of negative number raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.square_root(-4)
        self.assertIn("Cannot calculate square root of negative number", str(context.exception))

    def test_absolute(self):
        """Test absolute value operation."""
        self.assertEqual(self.calc.absolute(-5), 5)
        self.assertEqual(self.calc.absolute(5), 5)
        self.assertEqual(self.calc.absolute(0), 0)
        self.assertEqual(self.calc.absolute(-3.5), 3.5)

    def test_factorial(self):
        """Test factorial operation."""
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(10), 3628800)

    def test_factorial_negative(self):
        """Test factorial of negative number raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.factorial(-1)
        self.assertIn("Cannot calculate factorial of negative number", str(context.exception))

    def test_factorial_non_integer(self):
        """Test factorial of non-integer raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.factorial(3.5)
        self.assertIn("Factorial requires an integer", str(context.exception))

    def test_percentage(self):
        """Test percentage calculation."""
        self.assertEqual(self.calc.percentage(100, 50), 50)
        self.assertEqual(self.calc.percentage(200, 25), 50)
        self.assertEqual(self.calc.percentage(50, 10), 5)
        self.assertEqual(self.calc.percentage(0, 50), 0)

    def test_floor_divide(self):
        """Test floor division operation."""
        self.assertEqual(self.calc.floor_divide(10, 3), 3)
        self.assertEqual(self.calc.floor_divide(20, 4), 5)
        self.assertEqual(self.calc.floor_divide(7, 2), 3)
        self.assertEqual(self.calc.floor_divide(-7, 2), -4)

    def test_floor_divide_by_zero(self):
        """Test floor division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.floor_divide(5, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))


class TestCalculateFunction(unittest.TestCase):
    """Test cases for the calculate helper function."""

    def test_calculate_add(self):
        """Test calculate function with add operation."""
        self.assertEqual(calculate('add', 2, 3), 5)

    def test_calculate_multiply(self):
        """Test calculate function with multiply operation."""
        self.assertEqual(calculate('multiply', 4, 5), 20)

    def test_calculate_unknown_operation(self):
        """Test calculate function with unknown operation."""
        with self.assertRaises(ValueError) as context:
            calculate('unknown', 1, 2)
        self.assertIn("Unknown operation", str(context.exception))

    def test_calculate_square_root(self):
        """Test calculate function with square_root operation."""
        self.assertEqual(calculate('square_root', 16), 4)

    def test_calculate_absolute(self):
        """Test calculate function with absolute operation."""
        self.assertEqual(calculate('absolute', -5), 5)


if __name__ == '__main__':
    unittest.main()
