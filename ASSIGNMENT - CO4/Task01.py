from decimal import Decimal, InvalidOperation

def process_mess_file(filename):
    total = Decimal("0.00")
    report_rows, rejected = [], []
    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            try:
                parts = [x.strip() for x in line.split(",")]
                if len(parts) != 3:
                    raise ValueError("expected 3 fields")
                reg, name, amount_text = parts
                if not reg or not name:
                    raise ValueError("missing register number or name")
                amount = Decimal(amount_text)
                if not amount.is_finite():
                    raise ValueError("amount must be finite")
                total += amount
                report_rows.append(f"{name} {amount:.2f}")
            except (ValueError, InvalidOperation) as error:
                rejected.append((line_number, line, str(error)))
    return report_rows, total, rejected

if __name__ == "__main__":
    rows, total, rejected = process_mess_file("mess_oct.txt")
    print("\n".join(rows))
    print(f"Total {total:.2f}")
    print("Rejected:", rejected)
