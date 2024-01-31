#!/usr/bin/env python3

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class inherits from BaseCaching and represents a caching system
    """

    def __init__(self):
        """ Initialize LFUCache instance
        """
        super().__init__()
        self.freq_count = {}
        self.usage_count = {}

    def put(self, key, item):
        """ Add an item to the cache using LFU algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self._discard_lfu()

        self.freq_count[key] = self.freq_count.get(key, 0) + 1
        self.usage_count[key] = 0
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item from cache based on key
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_count[key] += 1
        return self.cache_data[key]

    def _discard_lfu(self):
        """ Discard least frequently used item (LFU)
        """
        min_freq = min(self.freq_count.values())
        lfu_keys = [k for k, v in self.freq_count.items() if v == min_freq]
        lru_key = min(lfu_keys, key=lambda k: self.usage_count[k])

        del self.cache_data[lru_key]
        del self.freq_count[lru_key]
        del self.usage_count[lru_key]
        print("DISCARD:", lru_key)
