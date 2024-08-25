#!/usr/bin/env python3
"""
Asynchronous programming efficiency
"""

from asyncio import gather
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    All coroutines (async_comprehension) are waiting concurrently.
    asyncio.gather(): This method executes multiple coroutines in parallel.
    In this case, you are running async_comprehension()
    four times simultaneously.

    time.time() is used to get the time in seconds since the epoch.
    Subtracting start_time from end_time gives the total execution time.
    """
    start_time = time.time()
    await gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
