#!/usr/bin/env python3
'''Asynchronous Comprehension Module.
'''
from typing import List
import asyncio

# Import the async_generator coroutine from Task 0
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Create a list of 10 random nums using async comprehension.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    '''
    return [num async for num in async_generator()]
