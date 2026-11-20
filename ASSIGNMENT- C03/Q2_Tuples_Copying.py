"""Q2 - Tuples, mutability, aliasing and copying."""
import copy
import sys
import time

def main():
    rows, cols = 3, 4
    bad = [[0] * cols] * rows
    bad[0][1] = 7
    good = [[0 for _ in range(cols)] for _ in range(rows)]
    good[0][1] = 7
    print("bad :", bad)
    print("good:", good)
    print(bad[0] is bad[1], good[0] is good[1])

    stops = {(13.0827, 80.2707): "Chennai Central",
             (13.0418, 80.2341): "T. Nagar"}
    print(stops[(13.0418, 80.2341)])
    try:
        stops[[13.0418, 80.2341]] = "Invalid key"
    except TypeError as error:
        print("List key error:", error)

    original = [[1, 2], [3, 4]]
    alias = original
    shallow_slice = original[:]
    shallow_copy = copy.copy(original)
    deep = copy.deepcopy(original)
    original[0][0] = 99
    print("Alias sees change:", alias)
    print("Shallow copy shares inner list:", shallow_slice[0] is original[0])
    print("Deep copy independent:", deep[0] is original[0], deep)

    print("Tuple/list shallow size (1M references):",
          sys.getsizeof(tuple(range(1_000_000))),
          sys.getsizeof(list(range(1_000_000))))

    values = list(range(100_000))
    start = time.perf_counter(); t = tuple(values); tuple_create = time.perf_counter()-start
    start = time.perf_counter(); l = list(values); list_create = time.perf_counter()-start
    start = time.perf_counter(); _ = t[50_000]; tuple_index = time.perf_counter()-start
    start = time.perf_counter(); _ = l[50_000]; list_index = time.perf_counter()-start
    print(f"Creation seconds tuple/list: {tuple_create:.6f}/{list_create:.6f}")
    print(f"Index seconds tuple/list: {tuple_index:.8f}/{list_index:.8f}")

    mixed = ("stop-A", [10, 20])
    mixed[1].append(30)
    print("Tuple containing mutable list:", mixed)

if __name__ == "__main__":
    main()
