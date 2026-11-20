"""Q6 - Nested railway timetable and station index."""
import random
import time
import sys

TIMETABLE = {
    "12601": {"name": "Chennai Express", "stops": [
        ("Chennai", "06:00", "06:10"), ("Katpadi", "08:00", "08:05"),
        ("Jolarpettai", "09:30", "09:35"), ("Bengaluru", "12:00", "12:10")],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat"}},
    "12602": {"name": "Coastal Express", "stops": [
        ("Chennai", "07:00", "07:15"), ("Arakkonam", "08:20", "08:25"),
        ("Katpadi", "09:40", "09:45"), ("Coimbatore", "14:00", "14:10")],
        "days": {"Mon", "Wed", "Fri", "Sun"}},
    "12603": {"name": "Hill Passenger", "stops": [
        ("Vellore", "05:00", "05:05"), ("Katpadi", "05:30", "05:35"),
        ("Salem", "09:00", "09:10")], "days": {"Tue", "Thu", "Sat"}},
    "12604": {"name": "Southern Mail", "stops": [
        ("Chennai", "10:00", "10:10"), ("Villupuram", "12:00", "12:05"),
        ("Trichy", "15:00", "15:10")], "days": {"Daily"}},
    "12605": {"name": "Western Link", "stops": [
        ("Bengaluru", "08:00", "08:10"), ("Jolarpettai", "10:00", "10:05"),
        ("Katpadi", "11:30", "11:35")], "days": {"Mon", "Tue", "Wed", "Thu", "Fri"}}
}

def build_index(table):
    index = {}
    for train, info in table.items():
        for station, arrival, departure in info["stops"]:
            index.setdefault(station, []).append((train, departure))
    return index

def query_scan(table, station, day):
    result = []
    for train, info in table.items():
        if day in info["days"] or "Daily" in info["days"]:
            for stop, arrival, departure in info["stops"]:
                if stop == station:
                    result.append((train, info["name"], departure))
                    break
    return sorted(result, key=lambda item: item[2])

def query_index(table, index, station, day):
    result = []
    for train, departure in index.get(station, []):
        info = table[train]
        if day in info["days"] or "Daily" in info["days"]:
            result.append((train, info["name"], departure))
    return sorted(result, key=lambda item: item[2])

def main():
    index = build_index(TIMETABLE)
    print("Trains at Katpadi on Monday:")
    for row in query_index(TIMETABLE, index, "Katpadi", "Mon"):
        print(row)
    print("Unknown station:", query_index(TIMETABLE, index, "Unknown", "Mon"))
    print("Third stop departure of 12601:", TIMETABLE["12601"]["stops"][2][2])
    print("Index station count:", len(index))
    assert query_scan(TIMETABLE, "Katpadi", "Mon") == query_index(TIMETABLE, index, "Katpadi", "Mon")

    # Scalable synthetic benchmark
    print("Trains, scan_seconds, indexed_seconds")
    for n in (100, 1_000, 10_000):
        table = {}
        for i in range(n):
            table[str(i)] = {"name": f"Train {i}",
                "stops": [(f"Station{j%100}", "08:00", "08:05") for j in range(10)],
                "days": {"Mon", "Wed", "Fri"}}
        idx = build_index(table)
        start = time.perf_counter(); query_scan(table, "Station5", "Mon")
        scan_t = time.perf_counter()-start
        start = time.perf_counter(); query_index(table, idx, "Station5", "Mon")
        idx_t = time.perf_counter()-start
        print(n, f"{scan_t:.6f}", f"{idx_t:.6f}")
    print("Index shallow size (bytes):", sys.getsizeof(index))

if __name__ == "__main__":
    main()
