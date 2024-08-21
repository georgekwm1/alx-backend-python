#!/usr/bin/env python3

""" A coroutine called async_generator that takes no arguments."""
import asyncio
import random


async def async_generator() -> any:
    """ A coroutine that yields 10 numbers."""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
