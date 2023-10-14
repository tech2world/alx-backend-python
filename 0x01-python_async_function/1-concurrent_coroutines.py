#!/usr/bin/env python3
"""basics of async"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn multiple instances of wait_random coroutine and gather their results.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    delays.sort()
    return delays
