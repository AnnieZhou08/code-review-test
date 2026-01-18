"""
Configuration settings for the calculator application.
"""

# Maximum history size
MAX_HISTORY_SIZE = 100

# Precision for floating point operations
DECIMAL_PRECISION = 10

# Supported operations
SUPPORTED_SINGLE_OPS = ['square_root', 'absolute', 'factorial']
SUPPORTED_BINARY_OPS = ['add', 'subtract', 'multiply', 'divide', 'power', 'modulo', 'percentage', 'floor_divide']

# Error messages
ERROR_DIVIDE_BY_ZERO = "Cannot divide by zero"
ERROR_NEGATIVE_SQRT = "Cannot calculate square root of negative number"
ERROR_NEGATIVE_FACTORIAL = "Cannot calculate factorial of negative number"
ERROR_MODULO_ZERO = "Cannot perform modulo with zero"
