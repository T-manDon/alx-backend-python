#!/usr/bin/env python3
"""
Def Asynchronous Compreh
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects ten random numbers using an async comprehensing,
    then rtn the 10 random num.
    """
    return [n async for n in async_generator()]
