#!/usr/bin/env python3
"""Contains typed function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of mixed list of ints and floats as a float"""
    return float(sum(mxd_lst))