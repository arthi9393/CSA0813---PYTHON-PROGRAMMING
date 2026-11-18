"""Compare float and Decimal accumulation and measure execution time."""
from decimal import Decimal
from time import perf_counter

def measure(n):
    values = ["33.40"] * n
    start = perf_counter()
    ftotal = sum(float(x) for x in values)
    float_seconds = perf_counter() - start
    start = perf_counter()
    dtotal = sum((Decimal(x) for x in values), Decimal("0.00"))
    decimal_seconds = perf_counter() - start
    print(f"n={n:>7} float={ftotal:.12f} Decimal={dtotal:.2f} "
          f"difference={Decimal(str(ftotal))-dtotal} "
          f"float_s={float_seconds:.6f} decimal_s={decimal_seconds:.6f}")

if __name__ == "__main__":
    for size in (300, 6000, 150000):
        measure(size)
