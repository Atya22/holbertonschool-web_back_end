#!/usr/bin/env python3
"""Adding function with type annotations. """
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of the lengths of the elements in a list of strings.

    Args:
        lst (List[str]): The list of strings to be measured.

    Returns:
        List[int]: The list of lengths of the elements in the list of strings.
    """
    return [len(element) for element in lst]
