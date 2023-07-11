#!/usr/bin/env python3
"""From the previous file, import wait_n into 2-measure_runtime.py.
Create a measure_time function with integers n and max_delay as
arguments that measures the total execution time for wait_n(n, max_delay
and returns total_time / n. Your function should return a float."""


import asyncio
import random
import time


def measure_time(n, max_delay: int = 10) -> float:
    """The async function of the progrm"""
    timer = time.perf_counter()
    return timer
