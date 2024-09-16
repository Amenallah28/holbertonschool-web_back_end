#!/usr/bin/python3
""" BasicCache module that inherits from BaseCaching """
from base_caching import BaseCaching

class BasicCache(BaseCaching):
     """ Basic caching system with no limit """
     def put(self, key, item):
          """
        assign to the dictionary
        """
          if key is not None and item is not None:
               self.cache_data[key] = item

     def get(self, key):
        """
        return the value linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
        
               