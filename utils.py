"""
Utility functions for the calculator application.
"""

from typing import Union, List, Tuple, Optional
from calculator import Calculator


def calculate(operation: str, a: Union[int, float], b: Optional[Union[int, float]] = None) -> Union[int, float]:
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


def format_result(result: Union[int, float], precision: int = 2) -> Union[int, float]:
    """Format a calculation result for display."""
    if isinstance(result, float):
        return round(result, precision)
    return result


def validate_operands(a: Union[int, float], b: Optional[Union[int, float]] = None, operation: Optional[str] = None) -> bool:
    """Validate operands for a calculation."""
    if not isinstance(a, (int, float)):
        raise TypeError("First operand must be a number")
    if b is not None and not isinstance(b, (int, float)):
        raise TypeError("Second operand must be a number")
    return True


def batch_calculate(operations: List[Tuple]) -> List[Union[int, float]]:
    """
    Perform multiple calculations in batch.

    Args:
        operations: List of tuples (operation, a, b) or (operation, a) for unary ops

    Returns:
        List of results corresponding to each operation

    Example:
        batch_calculate([
            ('add', 2, 3),
            ('multiply', 4, 5),
            ('square_root', 16)
        ])
        # Returns: [5, 20, 4.0]
    """
    results = []
    for op_tuple in operations:
        if len(op_tuple) == 2:
            operation, a = op_tuple
            result = calculate(operation, a)
        elif len(op_tuple) == 3:
            operation, a, b = op_tuple
            result = calculate(operation, a, b)
        else:
            raise ValueError(f"Invalid operation tuple: {op_tuple}")
        results.append(result)
    return results


def chain_calculate(start_value: Union[int, float], operations: List[Tuple]) -> Union[int, float]:
    """
    Chain multiple operations where each result feeds into the next.

    Args:
        start_value: Initial value to start with
        operations: List of tuples (operation, operand) for binary ops or (operation,) for unary

    Returns:
        Final result after all operations

    Example:
        chain_calculate(10, [
            ('add', 5),      # 10 + 5 = 15
            ('multiply', 2), # 15 * 2 = 30
            ('square_root',) # sqrt(30) = 5.477...
        ])
    """
    result = start_value
    for op_tuple in operations:
        if len(op_tuple) == 1:
            operation = op_tuple[0]
            result = calculate(operation, result)
        elif len(op_tuple) == 2:
            operation, operand = op_tuple
            result = calculate(operation, result, operand)
        else:
            raise ValueError(f"Invalid operation tuple: {op_tuple}")
    return result
