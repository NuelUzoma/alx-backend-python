#!/usr/bin/env python3
"""A coroutine called async_generetor that takes no arguments
loops 10 times & each time asynchronously wait 1 second
then yield a random number between 0 and 10"""


import random
import asyncio
from typing import List


async def async_generator() -> List[float]:
    """The function of the program"""
    for i in range(10):
        number: float = random.uniform(0, 10)
        yield number
        await asyncio.sleep(1)
