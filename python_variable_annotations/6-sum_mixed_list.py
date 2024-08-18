#!/usr/bin/python3
"""Adding function with type annotations. """


def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    """
    Returns the sum of a list of mixed floats and ints.

    Args:
        mxd_lst (List[int, float]): A list of mixed floats and ints to sum.

    Returns:
        float: The sum of the list of mixed floats and ints.
    """
    return sum(mxd_lst)