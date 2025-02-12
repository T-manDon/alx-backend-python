#!/usr/bin/env python3
"""Module containing a function to convert a key and a numeric value into a key-value pair."""  

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a key-value pair where the key is a string and the value is the square of a number.

    Args:
        k (str): The key as a string.
        v (Union[int, float]): A numeric value to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared value.
    """
    return k, v ** 2
