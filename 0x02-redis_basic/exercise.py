#!/usr/bin/env python3
""" Create a Cache class. In the __init__ method, store an
instance of the Redis client as a private variable """
import redis
import uuid
from typing import Union

class Cache:
    """ class cache to cache data into redis"""
    def __init__(self):
        """ init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Create a store method that takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid),"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
