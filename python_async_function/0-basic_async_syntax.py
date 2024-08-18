#!/usr/bin/env python3
"""Module for basic async syntax example."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait a random number between 0 and max_delay."""
    wait_time = random.uniform(0, float(max_delay))
    await asyncio.sleep(wait_time)
    return wait_time
