#!/usr/bin/env python3
"""Creating asyncio tasks"""

import asyncio
from typing import List
import random

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn multiple instances of task_wait_random coroutine
    and gather their results.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.

    Returns:
        List[float]: A list of delays (float values) in ascending
        order without using sort().
    """
    delay_rand = [await task_wait_random(max_delay) for _ in range(n)]
    # delay_rand.sort()
    return delay_rand
