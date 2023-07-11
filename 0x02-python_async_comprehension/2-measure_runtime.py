#!/usr/bin/env python3
"""mport async_comprehension from the previous file and write
a measure_runtime coroutine that will execute async_comprehension four times
in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it."""


import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """The function of the program"""
    start_time: float = asyncio.get_running_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time: float = asyncio.get_running_loop().time()
    return end_time - start_time
