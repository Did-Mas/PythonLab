import timeit
from functools import lru_cache

@lru_cache(128)
def fib_c(n):
    if n < 2:
        return 1
    else:
        return fib_c(n-2) + fib_c(n-1)

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)


print(timeit.timeit('fib_c(10)', globals=globals()))
print(timeit.timeit('fib(10)', globals=globals()))