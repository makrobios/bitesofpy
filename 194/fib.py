from functools import lru_cache

@lru_cache
def cached_fib(n):
    if n < 2:
        return 1 if n else 0
    return cached_fib(n-1) + cached_fib(n-2)
