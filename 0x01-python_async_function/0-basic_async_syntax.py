#!/usr/bin/env python3
"""basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random
    delay between 0 and max_delay seconds.

    Args:
    max_delay (int, optional): Maximum delay in seconds. default = 10.

    Returns:
    float: Random delay between 0 and max_delay seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
