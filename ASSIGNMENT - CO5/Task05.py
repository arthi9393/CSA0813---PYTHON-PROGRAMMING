# Task 5: modular organisation example in one executable file.
def read_records(lines):
    records = []
    for line in lines:
        fields = [x.strip() for x in line.split(",")]
        if len(fields) == 3 and fields[2] in {"P", "A"}:
            records.append(fields)
    return records

def percentage(present, total):
    return (present / total * 100) if total else 0.0

def absent_three_consecutive(statuses):
    return any(statuses[i:i+3] == ["A", "A", "A"]
               for i in range(len(statuses)-2))

def write_summary(records, filename="attendance_summary.txt"):
    totals = {}
    for reg, date, status in records:
        item = totals.setdefault(reg, [0, 0])
        item[1] += 1
        item[0] += status == "P"
    with open(filename, "w", encoding="utf-8") as f:
        for reg, (present, total) in sorted(totals.items()):
            f.write(f"{reg}: {percentage(present, total):.2f}%\n")

if __name__ == "__main__":
    sample = ["192311001,2026-10-01,P",
              "192311001,2026-10-02,A",
              "192311001,2026-10-03,A",
              "192311001,2026-10-04,A"]
    records = read_records(sample)
    write_summary(records)
    statuses = [row[2] for row in records]
    print("Percentage:", f"{percentage(1, 4):.2f}%")
    print("Three consecutive absences:", absent_three_consecutive(statuses))
