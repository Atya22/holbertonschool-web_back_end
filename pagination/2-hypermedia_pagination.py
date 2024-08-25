#!/usr/bin/env python3
"""Hypermedia pagination"""


import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Parameters:
    - page (int): The page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
            self.__dataset = dataset[1:]  # Exclude header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of data from the dataset."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return a dictionary containing pagination details and the dataset page.

        Args:
        - page (int): The page number to retrieve (1-indexed).
        - page_size (int): The number of items per page.

        Returns:
        - Dict: A dictionary with pagination metadata and data.
        """
        data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        hyper_dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if (page < total_pages) else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

        return hyper_dict
