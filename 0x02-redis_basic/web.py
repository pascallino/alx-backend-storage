#!/usr/bin/env python3
""" Create a Cache class. In the __init__ method, store an
instance of the Redis client as a private variable """
import requests
from functools import wraps
import redis
import time


def cache_with_count(func):
    """ wrapper cache count """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """ wrapper cache count func """
        # Assuming the first argument is the URL
        url = args[0]
        redis_instance = redis.Redis()

        # Key to store the count
        count_key = f"count:{url}"
        # Key to store the cached result
        cache_key = f"cache:{url}"

        # Check if result is cached
        cached_result = redis_instance.get(cache_key)
        if cached_result:
            # If cached, increment the count and return the cached result
            redis_instance.incr(count_key)
            return cached_result.decode('utf-8')

        # If not cached, call the original function
        result = func(*args, **kwargs)

        # Cache the result with a 10-second expiration
        redis_instance.setex(cache_key, 10, result)
        # Increment the count
        redis_instance.incr(count_key)

        return result

    return wrapper


@cache_with_count
def get_page(url: str) -> str:
    """ get page url"""
    response = requests.get(url)
    return response.text


# Example usage
if __name__ == "__main__":
    """ tester  """
    slow_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
    fast_url = "http://www.google.com"

    # Access slow URL multiple times to test caching and count tracking
    for _ in range(3):
        print(get_page(slow_url))

    # Access fast URL multiple times to test caching and count tracking
    for _ in range(3):
        print(get_page(fast_url))

    # Wait for 11 seconds to ensure cache expiration
    time.sleep(11)
