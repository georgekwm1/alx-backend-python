#!/usr/bin/env python3

""" Return the list of all the delays"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays (float values)"""
    # await asyncio.sleep(max_delay)
    new_list = []
    task = asyncio.create_task(wait_random(max_delay))
    res = await asyncio.gather(*(task for i in range(n)))
    for val in res:
        new_list.append(val)
    list_len = len(new_list)

    for i in range(list_len):
        for j in range(0, list_len-i-1):
            if new_list[j] > new_list[j+1]:
                # Swap the elements
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
    return new_list
