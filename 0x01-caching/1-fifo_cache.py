#!/usr/bin/env python3
"""FIFO caching
"""

from typing import Dict
BaseCaching = __import__('base_caching').BaseCaching


def delete_first_elem(d: Dict):
    """deletes the first element in a dictionary

    Args:
        d (_type_): dictionary
    """
    if d:
        first_key = next(iter(d))
        del d[first_key]
        print(f"DISCARD: {first_key}")


class FIFOCache(BaseCaching):
    """FIFO: inherits from BaseCaching and is a caching system:

    Args:
        BaseCaching (_type_): inherited class
    """
    def __init__(self):
        """constructor
        """
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value
           for the key key.

        Args:
            key (_type_): key
            item (_type_): value
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                delete_first_elem(self.cache_data)

    def get(self, key):
        """Get an item by key

        Args:
            key (_type_): key item

        Returns:
            _type_: return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
