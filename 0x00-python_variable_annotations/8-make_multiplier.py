#!/usr/bin/env python3
"""A type-annontated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """The callable function of the program"""
    def multiplier_func(num: float) -> float:
        """The function which will be multiplied by the callable function"""
        return (num * multiplier)
    return (multiplier_func)
