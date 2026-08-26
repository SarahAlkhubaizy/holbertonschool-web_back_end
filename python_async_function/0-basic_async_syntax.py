#!/usr/bin/env python3
"""Module for the task_wait_n coroutine."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times with the given max_delay.

    Returns a list of the resulting delays, sorted in ascending
    order (unlike wait_n, ordering here comes from asyncio.Task
    scheduling rather than plain coroutines).
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
