"""Interactive entry program for the Ksheera co-operative."""
from decimal import Decimal
from milkrate import validate_entry, payout, ten_day_total

def main():
    entries = []
    print("Ksheera Co-operative - ten-day payment entry")
    count = int(input("Number of entries: "))
    for index in range(count):
        print(f"\nEntry {index + 1}")
        while True:
            try:
                farmer_id = input("Farmer ID: ").strip()
                litres = Decimal(input("Litres: ").strip())
                fat = Decimal(input("Fat %: ").strip())
                snf = Decimal(input("SNF %: ").strip())
                shift = input("Shift (M/E): ").strip().upper()
                validate_entry(farmer_id, litres, fat, snf, shift)
                break
            except (ValueError, ArithmeticError) as error:
                print("Invalid entry:", error, "- please re-enter this farmer.")
        amount = payout(litres, fat, snf)
        entries.append({"farmer_id": farmer_id, "litres": litres,
                        "fat": fat, "snf": snf, "shift": shift})
        print(f"Rate/payment: Rs {amount / litres:.2f} / Rs {amount:.2f}")
    print(f"\nTen-day total: Rs {ten_day_total(entries):.2f}")

if __name__ == "__main__":
    main()
