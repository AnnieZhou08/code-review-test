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


def calculate(operation, a, b=None):
    """
    Perform a calculation based on the operation string.

    Args:
        operation: String representing the operation (add, subtract, multiply, divide, power, modulo)
        a: First operand
        b: Second operand

    Returns:
        Result of the calculation

    Raises:
        ValueError: If operation is not recognized
    """
    calc = Calculator()

    # Single operand operations
    single_ops = {
        'square_root': calc.square_root,
        'absolute': calc.absolute
    }

    # Two operand operations
    binary_ops = {
        'add': calc.add,
        'subtract': calc.subtract,
        'multiply': calc.multiply,
        'divide': calc.divide,
        'power': calc.power,
        'modulo': calc.modulo
    }

    if operation in single_ops:
        return single_ops[operation](a)
    elif operation in binary_ops:
        if b is None:
            raise ValueError(f"Operation '{operation}' requires two operands")
        return binary_ops[operation](a, b)
    else:
        raise ValueError(f"Unknown operation: {operation}")
