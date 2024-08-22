#!/usr/bin/env python3
"""0. Simple helper function"""


def index_range(page: int, page_size: int):
    """_summary_

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        Tuple: a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
    """
    if page == 0:
        page = 1

    count = page_size * page
    start = 0
    end = -1
    limit = round(count / page_size)
    for _ in range(limit):
        start = end + 1
        end += page_size

    end += 1
    return (start, end)
