#!/usr/bin/env python3
"""
Module containing a function that calculates the sum of a list containing both integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of numbers (integers and floats).

    Returns:
        float: The sum of all numbers in the list, returned as a float.
    """
    return sum(mxd_lst)
