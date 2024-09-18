#!/usr/bin/python3
""" FIFOCache module that inherits from BaseCaching """
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFO Cache class
    """
    def __init__(self):
        """
        overload
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        dictionary
        """
        if key is None or item is None:
            return
        
        if key not in self.cache_data:
            self.order.append(key)
        self.chache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """ 
        Retrieve an item from the cache
        """
        return self.cache_data.get(key, None)

