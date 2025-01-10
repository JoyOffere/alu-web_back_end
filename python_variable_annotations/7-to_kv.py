#!/usr/bin/env python3
"""Contains typed function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns tuple of string and square of number"""
    return (k, float(v ** 2))
