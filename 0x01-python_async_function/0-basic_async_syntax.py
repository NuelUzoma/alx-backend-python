#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that wiats for a random delay between 0 and max_delay
(included and float value) seconds and eventually return it."""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """The asynchronuos function for the program"""
    number = random.uniform(0, max_delay)
    await asyncio.sleep(number)
    return (number)
