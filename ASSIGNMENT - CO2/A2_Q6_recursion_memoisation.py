from functools import lru_cache
import sys

calls = 0
def ways_naive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n-1) + ways_naive(n-2)

@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n-1) + ways_memo(n-2)

def ways_loop(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

for n in range(1, 7):
    print(f"n={n}: {ways_loop(n)} ways")
calls = 0
print("naive:", ways_naive(25), "calls =", calls)
calls = 0
ways_memo.cache_clear()
print("memo :", ways_memo(25), "calls =", calls)
print("loop n=1000 digits:", len(str(ways_loop(1000))))
print("Recursion limit:", sys.getrecursionlimit())
print("For n=1000, iterative computation avoids recursion-depth failure.")
