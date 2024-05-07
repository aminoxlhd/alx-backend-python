#!/usr/bin/env python3
"""coroutine called async_comprehension that takes no arguments."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async_generator function"""
    return [random async for random in async_generator()]
