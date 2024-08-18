#!/usr/bin/env python3
"""Adding function with type annotations. """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a multiplier.

    Args:
        multiplier (float): The float to multiply by.

    Returns:
        Callable[[float], float]: A function that multiplies a float
        by a multiplier.
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
