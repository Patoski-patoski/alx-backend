#!/usr/bin/env python3
"""Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache: that inherits from BaseCaching and is a caching system:

    Args:
        BaseCaching (_type_): inherited class
    """

    def put(self, key, item):
        """_summary_: assign to the dictionary self.cache_data the item value
          for the key

        Args:
            key (_type_): _description_
            item (_type_): _description_

        Returns:
            _type_: _description_: nothing
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key

        Args:
            key (_type_): key item

        Returns:
            _type_: return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
