#!/usr/bin/env python3
"""LIFO caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache
    """

    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.keys = []
        self.last = None

    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.last = None

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last = self.last
                del self.cache_data[last]
                print("DISCARD: {}".format(last))
            self.last = key

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key, None)
