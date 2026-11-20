"""Q3 - Complaint word-frequency analysis with dictionaries and Counter."""
import random
import re
import time
from collections import Counter, defaultdict

CALLS = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received",
]
STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}
    for text in texts:
        for word in re.findall(r"[a-z]+", text.lower()):
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts

def top(counts, k):
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]

def group_by_district(records):
    grouped = defaultdict(list)
    for district, crop, complaint in records:
        grouped[district].append((crop, complaint))
    return dict(grouped)

def benchmark():
    random.seed(5)
    vocabulary = ["seed", "water", "pest", "price", "crop", "soil", "subsidy"]
    print("complaints, dict_seconds, list_count_seconds, Counter_seconds")
    for n in (1_000, 10_000, 100_000):
        texts = [" ".join(random.choices(vocabulary, k=8)) for _ in range(n)]
        words = [w for line in texts for w in line.split()]
        start = time.perf_counter(); frequencies(texts, set()); td = time.perf_counter()-start
        start = time.perf_counter()
        distinct = set(words)
        list_counts = {w: words.count(w) for w in distinct}
        tl = time.perf_counter()-start
        start = time.perf_counter(); Counter(words); tc = time.perf_counter()-start
        print(f"{n}, {td:.6f}, {tl:.6f}, {tc:.6f}")

def main():
    print(top(frequencies(CALLS, STOP), 3))
    records = [
        ("Thiruvallur", "rice", "Water supply delayed"),
        ("Chennai", "cotton", "Pest attack reported"),
        ("Thiruvallur", "rice", "Seed subsidy query"),
    ]
    grouped = group_by_district(records)
    print("Complaints by district:", {k: len(v) for k, v in grouped.items()})
    print("Empty input:", frequencies([""], STOP))
    print("Case/punctuation:", frequencies(["SEEDS, seeds!"], STOP))
    benchmark()

if __name__ == "__main__":
    main()
