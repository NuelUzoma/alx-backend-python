#!/usr/bin/env python3
"""A program that takes a list input_list of floats as argument
and returns their sum as a float."""


import math
from typing import List


def sum_list(input_list: List[float]) -> float:
    """The function which will return the sum of floats in the list"""
    return math.fsum(input_list)
