#!/usr/bin/env python3
"""Adding function with type annotations. """
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats to sum.

    Returns:
        float: The sum of the list of floats.
    """
    return sum(input_list)
