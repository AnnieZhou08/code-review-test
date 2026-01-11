"""
A simple calculator module for basic arithmetic operations.
"""


class Calculator:


    def add(self, a, b):
        """Add two numbers."""
        return a + b
    """Calculator class with basic arithmetic operations -- MODIFIED!."""
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


def calculate(operation, a, b):
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
    operations = {
        'add': calc.add,
        'subtract': calc.subtract,
        'multiply': calc.multiply,
        'divide': calc.divide,
        'power': calc.power,
        'modulo': calc.modulo
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return operations[operation](a, b)
