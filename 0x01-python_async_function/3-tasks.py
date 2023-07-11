#!/usr/bin/python3
"""Write a function (do not create an async function, use the regular function
yntax to do this) task_wait_random that takes an integer max_delay
and returns a asyncio.Task."""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """The function for the program"""
    number = wait_random(max_delay)
    return asyncio.Task(number)