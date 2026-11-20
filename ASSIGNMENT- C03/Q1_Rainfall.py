"""Q1 - Daily rainfall records: lists, slicing and moving averages."""
import random
import time

def weekly_totals(readings):
    return [sum(readings[i:i + 7]) for i in range(0, len(readings), 7)]

def moving_average_naive(values, window=7):
    if window <= 0:
        raise ValueError("window must be positive")
    return [sum(values[i:i + window]) / window
            for i in range(len(values) - window + 1)]

def moving_average_running(values, window=7):
    if window <= 0:
        raise ValueError("window must be positive")
    if len(values) < window:
        return []
    current = sum(values[:window])
    result = [current / window]
    for i in range(window, len(values)):
        current += values[i] - values[i - window]
        result.append(current / window)
    return result

def benchmark():
    random.seed(42)
    print("N, naive_seconds, running_seconds")
    for n in (365, 36_500, 365_000):
        data = [random.uniform(0, 80) for _ in range(n)]
        start = time.perf_counter()
        a = moving_average_naive(data)
        naive = time.perf_counter() - start
        start = time.perf_counter()
        b = moving_average_running(data)
        running = time.perf_counter() - start
        assert len(a) == len(b) and all(abs(x-y) < 1e-9 for x, y in zip(a, b))
        print(f"{n}, {naive:.6f}, {running:.6f}")

def main():
    random.seed(10)
    readings = [round(random.uniform(0, 80), 1) for _ in range(365)]
    weeks = weekly_totals(readings)
    wettest = max(range(len(weeks)), key=weeks.__getitem__)
    driest = min(range(len(weeks)), key=weeks.__getitem__)
    averages = moving_average_running(readings)
    dry_days = [i + 1 for i, value in enumerate(readings) if value == 0]
    print("First 5 weekly totals:", weeks[:5])
    print("Wettest week:", wettest + 1, "total =", weeks[wettest])
    print("Driest week:", driest + 1, "total =", weeks[driest])
    print("First 5 moving averages:", [round(x, 2) for x in averages[:5]])
    print("Dry days:", dry_days)
    print("Edge tests:", moving_average_running([]), moving_average_running([1, 2, 3]))
    benchmark()

if __name__ == "__main__":
    main()
