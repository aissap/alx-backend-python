#!/usr/bin/env python3
'''Async Generator Module.'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''Generate a sequence of random numbers asynchronously.

    Generate a sequence of 10 random numbers between 0 and 10,
    waiting for 1 second between each generation.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
