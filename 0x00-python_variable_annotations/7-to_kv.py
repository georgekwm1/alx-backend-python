#!/usr/bin/env python3
"""Define  a type-annotated function  that takes a string
and an int OR float as arguments and returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the key and value"""
    return (k, v**2)
