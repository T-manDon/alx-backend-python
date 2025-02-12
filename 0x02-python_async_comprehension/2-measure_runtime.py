#!/usr/bin/env python3
"""
Defs concurrency of 4 Asynchronous Compre opers
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Collect 10 random numbers with an async compreh,
    then return the 10 random num.
    """
    start: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end: float = time.perf_counter()
    return (end - start)
