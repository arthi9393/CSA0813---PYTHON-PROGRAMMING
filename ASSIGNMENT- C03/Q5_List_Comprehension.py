"""Q5 - Clean temperature sensor readings and compare approaches."""
import random
import sys
import time

def loop_clean(readings):
    valid = []
    for c in readings:
        if -50 <= c <= 50:
            valid.append(c)
    return valid

def comprehension_clean(readings):
    return [c for c in readings if -50 <= c <= 50]

def functional_clean(readings):
    return list(filter(lambda c: -50 <= c <= 50, readings))

def main():
    readings = [1.5, 3.0, 9.2, 55.0, -60.0, 6.5, 1.0, 4.0]
    loop = loop_clean(readings)
    comp = comprehension_clean(readings)
    functional = functional_clean(readings)
    assert loop == comp == functional
    fahrenheit = [c * 9 / 5 + 32 for c in comp]
    alarms = [(minute, c) for minute, c in enumerate(readings)
              if -50 <= c <= 50 and not 2 <= c <= 8]
    print("Valid Celsius:", loop)
    print("Fahrenheit:", [round(x, 2) for x in fahrenheit])
    print("Alarm minutes (zero-based):", alarms)
    print("All versions equal:", loop == comp == functional)

    print("N, loop_seconds, comprehension_seconds, filter_seconds")
    random.seed(7)
    for n in (10_000, 100_000, 1_000_000):
        data = [random.uniform(-60, 60) for _ in range(n)]
        timings = []
        for fn in (loop_clean, comprehension_clean, functional_clean):
            start = time.perf_counter(); result = fn(data)
            timings.append(time.perf_counter()-start)
        print(n, *(f"{x:.6f}" for x in timings))
    generator = (x for x in readings if -50 <= x <= 50)
    list_result = [x for x in readings if -50 <= x <= 50]
    print("Container sizes (bytes):", sys.getsizeof(list_result), sys.getsizeof(generator))
    print("All-valid/all-invalid:", len(comprehension_clean([2, 3, 4])),
          len(comprehension_clean([100, -100])))

if __name__ == "__main__":
    main()
