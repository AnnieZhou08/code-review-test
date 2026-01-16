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

    def clear(self) -> None:
        """Clear all history."""
        self._history = []

    def export_as_string(self) -> str:
        """
        Export history as a formatted string.

        Returns:
            Formatted string representation of all calculations
        """
        if not self._history:
            return "No calculation history"

        lines = ["Calculation History:", "=" * 50]
        for i, entry in enumerate(self._history, 1):
            op = entry['operation']
            operands = entry['operands']
            result = entry['result']
            operands_str = ', '.join(str(x) for x in operands)
            lines.append(f"{i}. {op}({operands_str}) = {result}")
        return '\n'.join(lines)

    def __len__(self) -> int:
        """Return the number of entries in history."""
        return len(self._history)

    def __repr__(self) -> str:
        """Return a developer-friendly representation."""
        return f"CalculationHistory(size={len(self._history)}, max_size={self._max_size})"
