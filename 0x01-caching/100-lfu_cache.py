#!/usr/bin/env python3
"""
100-lfu_cache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update frequency for LFU
                self.frequency[key] += 1
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least frequency used item (LFU algorithm)
                min_freq = min(self.frequency.values())
                least_freq_keys = [
                        k for k, v in self.frequency.items() if v == min_freq
                        ]

                if len(least_freq_keys) > 1:
                    lru_key = min(
                            self.cache_data,
                            key=lambda k: self.cache_data[k]["last_used"]
                            )
                    least_freq_keys = [lru_key]

                discarded_key = least_freq_keys[0]
                del self.cache_data[discarded_key]
                del self.frequency[discarded_key]
                print("DISCARD:", discarded_key)

            # Update cache and frequency
            self.cache_data[key] = {
                "item": item,
                "last_used": 0
            }
            self.frequency[key] = 1

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            # Update frequency and last_used for LFU
            self.frequency[key] += 1
            self.cache_data[key]["last_used"] += 1
            return self.cache_data[key]["item"]
        return None
