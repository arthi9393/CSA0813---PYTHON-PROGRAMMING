import time

items = [f"Item{i}:Rs{i % 50}" for i in range(10000)]

def build_plus(parts):
    result = ""
    for part in parts:
        result += part + ";"
    return result

def build_join(parts):
    return ";".join(parts) + ";"

def build_fstring(parts):
    return "".join(f"{part};" for part in parts)

for size in (1000, 10000):
    data = items[:size]
    timings = {}
    outputs = {}
    for name, fn in (("plus", build_plus), ("join", build_join), ("f-string", build_fstring)):
        start = time.perf_counter()
        outputs[name] = fn(data)
        timings[name] = time.perf_counter() - start
    print(f"Lines: {size}; same output: {len(set(outputs.values())) == 1}")
    print("  " + " | ".join(f"{k}: {v:.6f} s" for k,v in timings.items()))
print("join() builds from an iterable of parts and avoids repeated immutable-string rebuilding.")
