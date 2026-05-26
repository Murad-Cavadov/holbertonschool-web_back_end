#!/usr/bin/env python3
"""
This module provides a coroutine 'async_comprehension' that uses an
async comprehension to collect data from an asynchronous generator.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using an async
    comprehension and returns them as a list of floats.
    """
    return [i async for i in async_generator()]
