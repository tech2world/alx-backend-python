#!/usr/bin/env python3
"""basics of sync"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n"""
    start = time.time()
    await asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n
