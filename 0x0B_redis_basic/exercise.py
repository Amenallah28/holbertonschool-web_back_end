#!/usr/bin/env python3
"""
exercic file
"""
from typing import Union
import uuid
import redis

class Cache:
    def __init__(self):
        """constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self,data:Union[str,bytes,int,float]) -> str:
        """store the data in the redis with a randomly generated key"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key,data)
        
        return random_key
    