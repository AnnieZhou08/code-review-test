"""
Example usage of the calculator module.
"""

from calculator import Calculator, calculate


def main():
    """Demonstrate calculator functionality."""
    print("Calculator Demo")
    print("=" * 50)

    calc = Calculator()

    # Basic operations
    print("\nBasic Operations:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")
    print(f"17 % 5 = {calc.modulo(17, 5)}")

    # Using the calculate function
    print("\nUsing calculate() function:")
    print(f"calculate('add', 100, 50) = {calculate('add', 100, 50)}")
    print(f"calculate('multiply', 12, 12) = {calculate('multiply', 12, 12)}")

    # Error handling demo
    print("\nError Handling:")
    try:
        result = calc.divide(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")

    try:
        result = calculate('invalid', 1, 2)
    except ValueError as e:
        print(f"Error caught: {e}")

    print("\n" + "=" * 50)
    print("Demo complete!")


if __name__ == "__main__":
    main()
