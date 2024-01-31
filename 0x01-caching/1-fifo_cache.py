#!/usr/bin/env python3
"""
1-fifo_cache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """

    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the first item (FIFO algorithm)
                discarded_key, _ = next(iter(self.cache_data.items()))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
