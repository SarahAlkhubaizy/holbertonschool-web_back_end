#!/usr/bin/env python3
"""Module for the measure_runtime coroutine."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure total runtime of four parallel async_comprehension calls.

    Executes async_comprehension four times concurrently using
    asyncio.gather and returns the total elapsed time in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time = time.time()
    return end_time - start_time
