#!/usr/bin/env python3
"""LRU caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU cache
    """

    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                first = self.keys.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """Get an item by key
        """
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key, None)
