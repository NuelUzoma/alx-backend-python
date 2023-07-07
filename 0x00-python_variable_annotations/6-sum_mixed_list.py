#!/usr/bin/env python3
"""A type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float."""


from typing import List, Union
import math


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """The function of the program that will return a float"""
    return math.fsum(mxd_list)
