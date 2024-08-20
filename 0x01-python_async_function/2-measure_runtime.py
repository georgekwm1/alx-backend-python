#!/usr/bin/env python3

""" Defines a measure_time function with integers n and
 max_delay as arguments that measures the total execution
time for wait_n(n, max_delay), and returns total_time / n"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """returns the execution time of a function"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
