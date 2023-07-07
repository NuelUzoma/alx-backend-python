#!/usr/bin/env python3
"""Annotation of the given code with appropriate types
The code is given below"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """The function of the program"""
    if lst:
        return lst[0]
    else:
        return None
