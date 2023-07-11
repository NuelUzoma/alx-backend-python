#!/usr/bin/env python3
"""Import wait_n and alter it into a new function task_wait_n
The code is nearly identical to wait_n except task_wait_random
is being called"""


import asyncio
import random
from typing import List, Tuple
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """The function of the program"""
    delays: List[int] = [max_delay] * n
    results: List[float] = []
    coroutines: List[asyncio.Task] = [
            task_wait_random(delay) for delay in delays
            ]
    for coroutine in asyncio.as_completed(coroutines):
        result: Tuple[float, int] = await coroutine
        results.append(result[0])
    return (results)
