"""
A simple calculation history tracker.
"""

from typing import Dict, List, Union, Any


class CalculationHistory:
    """Tracks calculation history for the calculator."""

    def __init__(self, max_size: int = 100) -> None:
        """Initialize history with optional max size."""
        self._history: List[Dict[str, Any]] = []
        self._max_size = max_size

    def add(self, operation: str, operands: List[Union[int, float]], result: Union[int, float]) -> None:
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

    def get_last(self, n: int = 1) -> List[Dict[str, Any]]:
        """Get the last n calculations."""
        return self._history[-n:]

    def get_all(self) -> List[Dict[str, Any]]:
        """Get all calculations in history."""
        return self._history.copy()

    def filter_by_operation(self, operation: str) -> List[Dict[str, Any]]:
        """
        Filter history by operation type.

        Args:
            operation: The operation name to filter by

        Returns:
            List of history entries matching the operation
        """
        return [entry for entry in self._history if entry['operation'] == operation]

    def search_by_result(self, result: Union[int, float], tolerance: float = 0.0001) -> List[Dict[str, Any]]:
        """
        Search history for entries with a specific result.

        Args:
            result: The result value to search for
            tolerance: Tolerance for floating point comparison

        Returns:
            List of history entries with matching result
        """
        matches = []
        for entry in self._history:
            if isinstance(entry['result'], float) and isinstance(result, float):
                if abs(entry['result'] - result) <= tolerance:
                    matches.append(entry)
            elif entry['result'] == result:
                matches.append(entry)
        return matches

    def get_statistics(self) -> Dict[str, Union[int, Dict[str, int]]]:
        """
        Get statistics about the calculation history.

        Returns:
            Dictionary with statistics about operations
        """
        if not self._history:
            return {'total': 0, 'operations': {}}

        stats: Dict[str, Union[int, Dict[str, int]]] = {
            'total': len(self._history),
            'operations': {}
        }

        for entry in self._history:
            op = entry['operation']
            ops_dict = stats['operations']
            if isinstance(ops_dict, dict):
                if op not in ops_dict:
                    ops_dict[op] = 0
                ops_dict[op] += 1

        return stats

    def clear(self):
        """Clear all history."""
        self._history = []

    def __len__(self):
        """Return the number of entries in history."""
        return len(self._history)
