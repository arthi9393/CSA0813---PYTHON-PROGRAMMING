from pathlib import Path
import csv

def monthly_report(folder="."):
    counts = {}
    errors = []
    for path in sorted(Path(folder).glob("*.txt")):
        try:
            with path.open("r", encoding="utf-8") as f:
                for line_no, line in enumerate(f, 1):
                    if not line.strip():
                        continue
                    parts = [x.strip() for x in line.split(",")]
                    if len(parts) != 3 or parts[2] not in {"P", "A"}:
                        errors.append((str(path), line_no, line.rstrip(), "invalid record"))
                        continue
                    reg, date, status = parts
                    item = counts.setdefault(reg, {"present": 0, "total": 0})
                    item["total"] += 1
                    item["present"] += status == "P"
        except (FileNotFoundError, PermissionError, UnicodeDecodeError, OSError) as error:
            errors.append((str(path), 0, "", f"{type(error).__name__}: {error}"))

    with open("monthly_attendance.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["register_number", "present_days", "total_days", "percentage"])
        for reg, item in sorted(counts.items()):
            pct = item["present"] / item["total"] * 100
            w.writerow([reg, item["present"], item["total"], f"{pct:.2f}"])

    with open("below_75.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["register_number", "percentage"])
        for reg, item in sorted(counts.items()):
            pct = item["present"] / item["total"] * 100
            if pct < 75:
                w.writerow([reg, f"{pct:.2f}"])

    with open("damaged_records.log", "w", encoding="utf-8") as f:
        for row in errors:
            f.write(" | ".join(map(str, row)) + "\n")
    return counts, errors

if __name__ == "__main__":
    counts, errors = monthly_report(".")
    print("Students processed:", len(counts))
    print("Damaged/file errors:", len(errors))
