#!/usr/bin/env python3
"""Asyncio Tasks"""

from asyncio import create_task
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """
    Create an asyncio Task.

    Args:
        max_delay (int): The maximum delay for the wait_random function.

    Returns:
        Any: An asyncio Task for the wait_random function.
    """
    task = create_task(wait_random(max_delay))
    return task
