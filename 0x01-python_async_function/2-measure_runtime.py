#!/usr/bin/env python3
"""
Module for measuring runtime
"""
import time
from typing import Callable
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the execution time for wait_n and returns total_time / n.

    Args:
        n : Number of times to call wait_n.
        max_delay : Maximum delay in seconds.

    Returns:
        float: Average execution time per call to wait_n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
