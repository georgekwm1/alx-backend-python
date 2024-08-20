#!/usr/bin/env python3
"""0-basic_async_syntax.py module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait_random function"""
    i = random.random() * max_delay
    await asyncio.sleep(i)
    return i
