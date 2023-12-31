#!/usr/bin/env python3
"""
FIFO cache class
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        super().__init__()
        self.cache_data

    def put(self, key, item):
        """Adds element and removes first element if cache is full"""
        if not key or not item:
            return
        self.cache_data.update({key: item})
        if len(self.cache_data.items()) > self.MAX_ITEMS:
            first_item = [x for x in self.cache_data.keys()]
            self.cache_data.pop(first_item[0])
            print("DISCARD: {}".format(first_item[0]))

    def get(self, key):
        """gets item from cache by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
