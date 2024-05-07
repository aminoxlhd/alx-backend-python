#!/usr/bin/env python3
"""coroutine called async_generator that takes no arguments."""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[int, None, None]:
    """async_generator function"""
    for a in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
