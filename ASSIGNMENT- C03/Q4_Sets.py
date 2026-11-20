"""Q4 - Elective registration clash detection using sets."""
import time

ai_elective = {"192311001", "192311004", "192311007", "192311009"}
iot_elective = {"192311002", "192311004", "192311009", "192311010"}
all_students = {f"1923110{i:02d}" for i in range(1, 11)}

def reports(ai, iot, all_ids):
    both = ai & iot
    exactly_one = ai ^ iot
    neither = all_ids - (ai | iot)
    return both, exactly_one, neither

def benchmark():
    print("N, list_membership_seconds, set_membership_seconds")
    for n in (10_000, 100_000, 1_000_000):
        values = list(range(n))
        value_set = set(values)
        target = n - 1
        start = time.perf_counter()
        for _ in range(1000): target in values
        list_time = time.perf_counter()-start
        start = time.perf_counter()
        for _ in range(1000): target in value_set
        set_time = time.perf_counter()-start
        print(f"{n}, {list_time:.6f}, {set_time:.6f}")

def main():
    both, exactly_one, neither = reports(ai_elective, iot_elective, all_students)
    print("clash :", sorted(both))
    print("exactly one:", sorted(exactly_one))
    print("neither :", sorted(neither))
    # Method-based equivalent
    method_results = (ai_elective.intersection(iot_elective),
                      ai_elective.symmetric_difference(iot_elective),
                      all_students.difference(ai_elective.union(iot_elective)))
    assert method_results == (both, exactly_one, neither)
    print("Set-method results match:", True)
    print("Empty test:", reports(set(), set(), {"A", "B"}))
    print("Identical test:", reports({"A", "B"}, {"A", "B"}, {"A", "B", "C"}))
    benchmark()

if __name__ == "__main__":
    main()
