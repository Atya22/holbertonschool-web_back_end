#!/usr/bin/env python3
"""Module for a function that returns an asyncio.Task.

This module defines a function `task_wait_random` that creates and returns 
an asyncio.Task for the `wait_random` coroutine with a specified maximum delay.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the `wait_random` coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for the `wait_random` call.

    Returns:
        asyncio.Task: An asyncio.Task object for the `wait_random` coroutine.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
