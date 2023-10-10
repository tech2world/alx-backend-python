#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write
a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.
"""

import asyncio
from time import time

async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel
    measure the total runtime and return it.
    """
    start_time = time()
    tasks = [async_comp() for _ in range(4)]
    await asyncio.gather(*tasks)
    stop_time = time()
    return (stop_time - start_time)
