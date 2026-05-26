#!/usr/bin/env python3
"""
This module provides an asynchronous generator coroutine that loops
10 times, waits asynchronously each time, and yields a random number.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times, asynchronously waits 1 second each iteration,
    then yields a random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
