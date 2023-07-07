#!/usr/bin/env python3
"""Use the parameters and the return values to add type annotations
to the function"""


from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    """The function to be used for annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
