#!/usr/bin/env python3
"""Contains typed function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns function that multiplies float by multiplier"""
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
