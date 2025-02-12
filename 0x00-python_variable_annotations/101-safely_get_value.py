#!/usr/bin/env python3
"""
Module containing a function to safely retrieve a value from a dictionary.
"""

from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')  # Generic type variable


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Retrieves a value from a dictionary safely, returning a default if the key is missing.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to look up in the dictionary.
        default (Optional[T], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value from the dictionary if the key exists; otherwise, the default value.
    """
    return dct[key] if key in dct else default
