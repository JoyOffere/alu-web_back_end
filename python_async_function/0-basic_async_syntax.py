#!/usr/bin/env python3
"""Contains async function wait_random"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits random time between 0 and max_delay seconds"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
