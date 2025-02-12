#!/usr/bin/env python3
"""
Defines a function that expands a tuple of integers by repeating each element a given number of times.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Expands a tuple by repeating each element a specified number of times.

    Args:
        lst (Tuple[int, ...]): A tuple of integers to be expanded.
        factor (int, optional): The number of times each element should be repeated. Defaults to 2.

    Returns:
        List[int]: A list where each element from the tuple is repeated 'factor' times.
    """
    zoomed_in: List[int] = [item for item in lst for _ in range(factor)]
    return zoomed_in


# Sample tuple of integers
array: Tuple[int, ...] = (12, 72, 91)

# Create lists with elements repeated twice and three times
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
