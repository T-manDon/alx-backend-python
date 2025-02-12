#!/usr/bin/env python3
""" Import wait_random frm prev python file that ive written and
    write an async routine called wait_n that takes in 2 int arguments:
    max_delay and n. You will spawn_random n times with the specified
    max_delay. wait_n should return the f all the delays (float values).
    The list of the delays should be in ascendorder without using sort()
    because of concurrency. """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Let's execute multiple coroutines at the same time with async  """
    delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays
