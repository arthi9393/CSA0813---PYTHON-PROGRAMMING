"""Repeatable validation tests. Run: py test_milkrate.py"""
from decimal import Decimal
from milkrate import (rate_per_litre, payout, validate_entry, whole_steps,
                      seasonal_payout, volume_bonus, final_ten_day_payment)

def run_tests():
    cases = [
        ("standard", rate_per_litre("3.5", "8.5"), Decimal("30.00")),
        ("fat and SNF above", rate_per_litre("4.2", "8.7"), Decimal("33.40")),
        ("fat and SNF below", rate_per_litre("3.1", "8.3"), Decimal("27.80")),
        ("minimum fat", rate_per_litre("2.0", "8.5"), Decimal("24.00")),
        ("maximum fat", rate_per_litre("7.0", "8.5"), Decimal("44.00")),
        ("payout sample", payout("8.5", "4.2", "8.7"), Decimal("283.90")),
        ("seasonal rate", seasonal_payout("1", "4.26", "8.76", "summer"),
         Decimal("36.50")),
        ("bonus above 500", volume_bonus("501"), Decimal("250.50")),
        ("no bonus at 500", volume_bonus("500"), Decimal("0.00")),
    ]
    for name, actual, expected in cases:
        assert actual == expected, f"{name}: expected {expected}, got {actual}"
        print(f"PASS | {name:20} | expected {expected} | actual {actual}")
    assert whole_steps("4.26", "3.5") == 8
    assert validate_entry("F001", "10", "3.5", "8.5", "M")
    for args in [("F1", "-1", "3.5", "8.5", "M"),
                 ("F1", "10", "7.1", "8.5", "M"),
                 ("F1", "10", "3.5", "8.5", "X")]:
        try:
            validate_entry(*args)
            raise AssertionError("Invalid input was accepted")
        except ValueError:
            print("PASS | invalid input rejected |", args)
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()
