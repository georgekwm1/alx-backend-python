#!/usr/bin/env python3

""" Return the list of all the delays"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays (float values)"""
    # await asyncio.sleep(max_delay)
    new_list = []
    res = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    for val in res:
        new_list.append(val)
    return new_list
