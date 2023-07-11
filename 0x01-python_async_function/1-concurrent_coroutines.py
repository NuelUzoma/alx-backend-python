#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve written
and write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random
n times with the specified max_delay"""


import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: float, max_delay: int = 10) -> float:
    """The async function of the program"""
    n = await wait_random(max_delay)
    numbers = random.randint(n, max_delay)
    return float(numbers)
