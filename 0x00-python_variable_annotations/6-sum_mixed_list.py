#!/usr/bin/env python3
"""Define a type-annotated function which takes a
list of integers and floats"""
from typing import List, Union
from functools import reduce


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and floats"""
    add_list = reduce(lambda x, y: float(x + y), mxd_lst)
    return add_list
