# Design challenge: redesign the naive recursive stair-count solution as an O(n) loop.
import time

def naive_count(n):
    if n <= 1:
        return 1
    return naive_count(n-1) + naive_count(n-2)

def iterative_count(n):
    if n <= 1:
        return 1
    previous, current = 1, 1
    for _ in range(2, n+1):
        previous, current = current, previous + current
    return current

print("Redesign: recursive repeated work -> iterative two-variable update")
for n in (5, 10, 20, 30):
    start = time.perf_counter()
    old = naive_count(n)
    old_time = time.perf_counter() - start
    start = time.perf_counter()
    new = iterative_count(n)
    new_time = time.perf_counter() - start
    print(f"n={n}: same={old == new}; recursive={old_time:.6f}s; iterative={new_time:.6f}s")
print("Trade-off: iterative version uses O(1) auxiliary space; recursive version is clearer for the recurrence.")
