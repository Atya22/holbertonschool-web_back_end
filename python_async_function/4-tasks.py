#!/usr/bin/env python3
"""Executes `task_wait_random` n times with max_delay seconds and returns results in order of completion."""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes `task_wait_random` n times with max_delay seconds.

    Args:
        n (int): The number of times to execute `task_wait_random`.
        max_delay (int): The maximum delay in seconds for each `task_wait_random` call.

    Returns:
        List[float]: A list of delays in the order they completed.
    """
    delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        min_result = await delay
        all_delays.append(min_result)
    return all_delays
