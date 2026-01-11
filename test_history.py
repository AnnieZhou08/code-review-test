"""
Unit tests for the history module.
"""

import unittest
from history import CalculationHistory


class TestCalculationHistory(unittest.TestCase):
    """Test cases for the CalculationHistory class."""

    def setUp(self):
        """Set up test fixtures."""
        self.history = CalculationHistory()

    def test_add_entry(self):
        """Test adding an entry to history."""
        self.history.add('add', (2, 3), 5)
        self.assertEqual(len(self.history), 1)

    def test_get_last(self):
        """Test getting the last entries."""
        self.history.add('add', (2, 3), 5)
        self.history.add('multiply', (4, 5), 20)
        last = self.history.get_last(1)
        self.assertEqual(last[0]['operation'], 'multiply')

    def test_clear(self):
        """Test clearing history."""
        self.history.add('add', (2, 3), 5)
        self.history.clear()
        self.assertEqual(len(self.history), 0)

    def test_max_size(self):
        """Test that history respects max size."""
        small_history = CalculationHistory(max_size=2)
        small_history.add('add', (1, 1), 2)
        small_history.add('add', (2, 2), 4)
        small_history.add('add', (3, 3), 6)
        self.assertEqual(len(small_history), 2)


if __name__ == '__main__':
    unittest.main()
