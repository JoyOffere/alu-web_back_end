#!/usr/bin/env python3
"""simple helper function"""


def index_range(page, page_size):
    """Return a simple helper function containing start and end index"""
    if (page == 1):
        return (0, page_size)
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
