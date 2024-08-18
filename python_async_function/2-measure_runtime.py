#!/usr/bin/env python3
"""Module to measure the runtime of the `wait_n` function."""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average runtime of the `wait_n` function.

    Args:
        n (int): The number of times to execute `wait_n`.
        max_delay (int): The maximum delay in seconds for each `wait_n` call.

    Returns:
        float: The average runtime per execution.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
