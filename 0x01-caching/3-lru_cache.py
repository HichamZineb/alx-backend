#!/usr/bin/env python3
"""
3-lru_cache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update order for LRU
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least recently used item (LRU algorithm)
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            # Update cache and order
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            # Update order for LRU
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
