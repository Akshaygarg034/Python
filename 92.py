# ************************  Function Caching in Python  ************************

# The functools module in Python provides a function called lru_cache, which is used to cache the result of a function. This is especially useful when the function is computationally expensive and the same result is needed multiple times. It is also called Memoization.

# Example:

import functools
import time

# maxSize is the maximum number of calls that will be cached. If None, there is no limit.
@functools.lru_cache(maxsize = None)
def computation(n):
    time.sleep(2)
    return n * n


print(computation(5))
print(computation(10))
print(computation(20))

print(computation(5))   # The result is returned immediately as it is cached
print(computation(10))   # The result is returned immediately as it is cached
print(computation(20))   # The result is returned immediately as it is cached

print(computation(25))   # The result is not returned immediately as it is not cached
