#!/usr/bin/env python3
""" 1-simple_pagination.py """
import csv
from typing import List


def index_range(page: int, page_size: int):
    """a function named index_range that takes two integer arguments page and
    page_size.

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


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Copy index_range from the previous task and the following class into
           your code

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]:  the appropriate page of the dataset
            (i.e. the correct list of rows).
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
