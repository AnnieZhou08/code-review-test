"""
A simple calculator module for basic arithmetic operations.
"""


class Calculator:
    """Calculator class with basic arithmetic operations."""

    def add(self, a, b):
        """Add two numbers."""
        return a + b
    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        """Raise a to the power of b."""
        return a ** b

    def modulo(self, a, b):
        """Return the remainder of a divided by b."""
        if b == 0:
            raise ValueError("Cannot perform modulo with zero")
        return a % b

    def square_root(self, a):
        """Return the square root of a."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return a ** 0.5

    def absolute(self, a):
        """Return the absolute value of a."""
        return abs(a)

    def factorial(self, n):
        """Return the factorial of n."""
        if n < 0:
            raise ValueError("Cannot calculate factorial of negative number")
        if not isinstance(n, int):
            raise ValueError("Factorial requires an integer")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def percentage(self, value, percent):
        """Calculate percent of value."""
        return (value * percent) / 100

    def floor_divide(self, a, b):
        """Return the floor division of a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a // b
