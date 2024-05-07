#!/usr/bin/env python3
"""
Module for creating asyncio tasks
"""
import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Take an integer max_delay and returns an asyncio.Task.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
