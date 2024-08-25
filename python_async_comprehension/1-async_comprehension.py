#!/usr/bin/env python3
"""
Async Comprehensions
"""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects the 10 numbers generated asynchronously by async_generator
    using an asynchronous compiler and returns that list.
    This list is printed on output.
    """
    return [i async for i in async_generator()]
