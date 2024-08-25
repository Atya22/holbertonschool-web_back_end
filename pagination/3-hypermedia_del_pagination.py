#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Deletion-resilient method to return page data with index.

        Args:
        - index (int): Current start index of the return page.
        - page_size (int): Number of items per page.

        Returns:
        - Dict: Dictionary containing pagination data.
        """
        assert index is not None and 0 <= index < len(self.indexed_dataset())

        indexed_d = self.indexed_dataset()
        data = []
        next_index = index

        for _ in range(page_size):
            while next_index not in indexed_d and next_index < len(indexed_d):
                next_index += 1
            if next_index < len(indexed_d):
                data.append(indexed_d[next_index])
                next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
