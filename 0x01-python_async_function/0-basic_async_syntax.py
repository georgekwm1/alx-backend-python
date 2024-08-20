#!/usr/bin/env python3
"""Defines an asynchronous coroutine that takes in an integer argument 
(max_delay) and returns a random float number between 0 and max_delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait_random function"""
    i = random.random() * max_delay
    await asyncio.sleep(i)
    return i
