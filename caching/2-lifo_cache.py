#!/usr/bin/python3
"""
LIFO caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Cache
    """

    def __init__(self):
        """
        overload
        """
        super().__init__()

    def put(self, key, item):
        """
        dictionary
        """
        if key and item :
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.remove)
            print (f"DISCARD: {self.remove}")
        if key :
              self.remove = key
        else:
            pass

    def get(self, key):
        """
        get value of key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
    
    

            

