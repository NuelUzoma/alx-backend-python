#!/usr/bin/env python3
"""Using the function, annontate its parameters and return values with
the appropriate types"""


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """The function for the program"""
    return [(i, len(i)) for i in lst]
