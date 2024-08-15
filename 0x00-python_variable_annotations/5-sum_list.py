#!/usr/bin/env python3
"""a type-annotated function which takes a list of floats as argument"""
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    """returns the sum of all elements in the list"""
    add_list = reduce(lambda x, y: x + y, input_list)
    return add_list
