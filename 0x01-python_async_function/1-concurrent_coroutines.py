#!/usr/bin/env python3

""" Return the list of all the delays"""
import asyncio
import time
import random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays (float values)"""
