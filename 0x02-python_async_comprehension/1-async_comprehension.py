#!/usr/bin/env python3

""" A coroutine called async_comprehension that takes no arguments."""
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """A coroutine that yields 10 numbers."""
    result = [i async for i in async_generator()]

    return result
