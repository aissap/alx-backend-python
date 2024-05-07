#!/usr/bin/env python3

'''Measure Runtime Module.'''

import asyncio
from typing import List
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measure the total runtime for four parallel comprehensions.
    Returns:
        float: Runtime for executing async_comprehension four times
               in parallel.
    '''
    start_time = perf_counter()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end_time = perf_counter()
    return end_time - start_time
