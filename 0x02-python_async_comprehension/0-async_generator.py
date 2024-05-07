#!/usr/bin/env python3
'''Async Generator Module.

This module defines an asynchronous generator coroutine that generates a
sequence of random numbers asynchronously.
'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''Generate a sequence of random numbers asynchronously.

    Generate a sequence of 10 random numbers between 0 and 10,
    waiting for 1 second between each generation.

    Yields:
        float: A random floating-point number between 0 and 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
