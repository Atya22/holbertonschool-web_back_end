#!/usr/bin/env python3
"""Module for basic concurrent coroutines."""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes `wait_random` n times with max_delay seconds.

    Args:
        n (int): The number of times to execute `wait_random`.
        max_delay (int): The maximum delay in seconds for each `wait_random` call.

    Returns:
        List[float]: A list of delays in the order they completed.
    """
    delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        min_result = await delay
        all_delays.append(min_result)
    return all_delays
