"""
A simple calculation history tracker.
"""


class CalculationHistory:
    """Tracks calculation history for the calculator."""

    def __init__(self, max_size=100):
        """Initialize history with optional max size."""
        self._history = []
        self._max_size = max_size

    def add(self, operation, operands, result):
        """Add a calculation to history."""
        entry = {
            'operation': operation,
            'operands': operands,
            'result': result
        }
        self._history.append(entry)

        # Trim if exceeds max size
        if len(self._history) > self._max_size:
            self._history = self._history[-self._max_size:]

    def get_last(self, n=1):
        """Get the last n calculations."""
        return self._history[-n:]

    def clear(self):
        """Clear all history."""
        self._history = []

    def __len__(self):
        """Return the number of entries in history."""
        return len(self._history)
