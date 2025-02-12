#!/usr/bin/env python3
"""Module containing a function that returns a multiplier function."""  

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a given number by a specified multiplier.

    Args:
        multiplier (float): The value by which numbers will be multiplied.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the result of multiplying it by the multiplier.
    """

    def multiplier_func(number: float) -> float:
        """
        Multiplies a given number by the predefined multiplier.

        Args:
            number (float): The number to be multiplied.

        Returns:
            float: The product of the number and the multiplier.
        """
        return multiplier * number

    return multiplier_func
