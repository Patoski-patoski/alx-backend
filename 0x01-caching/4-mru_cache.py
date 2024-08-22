#!/usr/bin/env python3
"""MRU caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU cache
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
                last = self.keys.pop(-2)
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

    def get(self, key):
        """Get an item by key
        """
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key, None)
