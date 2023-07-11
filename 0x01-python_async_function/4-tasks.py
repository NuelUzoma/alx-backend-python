#!/usr/bin/env python3
"""Import wait_n and alter it into a new function task_wait_n
The code is nearly identical to wait_n except task_wait_random
is being called"""


import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay) -> float:
    """The function of the program"""
    n = await task_wait_random(max_delay)
    numbers = random.randint(n, max_delay)
    return float(numbers)
