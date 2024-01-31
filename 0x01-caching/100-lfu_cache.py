#!/usr/bin/env python3
"""
100-lfu_cache module
"""

from collections import OrderedDict, defaultdict
from typing import Union


class LFUCache(BaseCaching):
    """ Defines an LFU caching system """

    def __init__(self):
        """ Initializes the LFU cache """
        super().__init__()
        self.frequency = defaultdict(int)
        self.last_used = OrderedDict()

    def put(self, key: Union[str, int], item: Union[str, int]) -> None:
        """ Adds an item to the LFU cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.frequency[key] += 1
        self.last_used[key] = 0

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self._discard_least_frequent()

    def get(self, key: Union[str, int]) -> Union[str, int, None]:
        """ Retrieves an item from the LFU cache """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.last_used[key] = 0
        return self.cache_data[key]

    def _discard_least_frequent(self) -> None:
        """ Discards the least frequent item from the LFU cache """
        min_freq = min(self.frequency.values())
        least_freq_keys = [
                k for k, v in self.frequency.items() if v == min_freq
                ]
        lfu_key = min(least_freq_keys, key=lambda k: self.last_used[k])

        self.cache_data.pop(lfu_key)
        self.frequency.pop(lfu_key)
        self.last_used.pop(lfu_key)
