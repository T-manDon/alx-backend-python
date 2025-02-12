#!/usr/bin/env python3
""" From the prev file, import wait_n to 2-measure_runtime.py.
    Create a measure_time func with int n and max_delay as argu
    that measures the total ex time for wait_n(n, max_delay), and
    returns total_time / n. Yr fun return a float.
    Use the time module to measure an approx elapsed time. """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
