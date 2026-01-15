"""
Utility functions for the calculator application.
"""

from calculator import Calculator


def calculate(operation, a, b=None):
    """
    Perform a calculation based on the operation string.

    Args:
        operation: String representing the operation
        a: First operand
        b: Second operand (optional for unary operations)

    Returns:
        Result of the calculation

    Raises:
        ValueError: If operation is not recognized
    """
    calc = Calculator()

    single_ops = {
        'square_root': calc.square_root,
        'absolute': calc.absolute,
        'factorial': calc.factorial
    }

    binary_ops = {
        'add': calc.add,
        'subtract': calc.subtract,
        'multiply': calc.multiply,
        'divide': calc.divide,
        'power': calc.power,
        'modulo': calc.modulo,
        'percentage': calc.percentage,
        'floor_divide': calc.floor_divide
    }

    if operation in single_ops:
        return single_ops[operation](a)
    elif operation in binary_ops:
        if b is None:
            raise ValueError(f"Operation '{operation}' requires two operands")
        return binary_ops[operation](a, b)
    else:
        raise ValueError(f"Unknown operation: {operation}")


def format_result(result, precision=2):
    """Format a calculation result for display."""
    if isinstance(result, float):
        return round(result, precision)
    return result


def validate_operands(a, b=None, operation=None):
    """Validate operands for a calculation."""
    if not isinstance(a, (int, float)):
        raise TypeError("First operand must be a number")
    if b is not None and not isinstance(b, (int, float)):
        raise TypeError("Second operand must be a number")
    return True
