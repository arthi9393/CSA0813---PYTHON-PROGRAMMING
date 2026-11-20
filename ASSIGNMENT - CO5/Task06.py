import csv
from pathlib import Path

class InvalidRegistration(Exception):
    pass

def validate_record(line):
    fields = [x.strip() for x in line.rstrip("\n").split(",")]
    if len(fields) != 5:
        raise InvalidRegistration(f"expected 5 fields, found {len(fields)}")
    reg, name, dept, email, events_text = fields
    if not all((reg, name, dept, email, events_text)):
        raise InvalidRegistration("required field is empty")
    if email.count("@") != 1:
        raise InvalidRegistration("e-mail must contain exactly one @")
    local, domain = email.split("@")
    if not local or not domain or "." not in domain or domain.startswith(".") or domain.endswith("."):
        raise InvalidRegistration("invalid e-mail address")
    events = [x.strip() for x in events_text.split(";") if x.strip()]
    if not events:
        raise InvalidRegistration("no events selected")
    return {"register_number": reg, "name": name, "department": dept,
            "email": email, "events": events}

def process_files(paths):
    seen, master, event_map, errors = set(), [], {}, []
    for path in map(Path, paths):
        try:
            with path.open(encoding="utf-8") as f:
                for line_no, line in enumerate(f, 1):
                    if not line.strip():
                        continue
                    try:
                        row = validate_record(line)
                        if row["register_number"] in seen:
                            raise InvalidRegistration(
                                f"duplicate register number {row['register_number']}")
                        seen.add(row["register_number"])
                        master.append(row)
                        for event in row["events"]:
                            event_map.setdefault(event, []).append(row)
                    except InvalidRegistration as error:
                        errors.append((str(path), line_no, str(error), line.rstrip()))
        except (FileNotFoundError, PermissionError, UnicodeDecodeError, OSError) as error:
            errors.append((str(path), 0, f"{type(error).__name__}: {error}", ""))

    return master, event_map, errors

def write_outputs(master, event_map, errors):
    fields = ["register_number", "name", "department", "email", "events"]
    with open("master_list.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
        for r in master: w.writerow({**r, "events": ";".join(r["events"])})
    for event, rows in event_map.items():
        safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in event)
        with open(f"event_{safe}.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
            for r in rows: w.writerow({**r, "events": ";".join(r["events"])})
    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Accepted registrations: {len(master)}\n")
        f.write(f"Events: {len(event_map)}\n")
        for event, rows in sorted(event_map.items()):
            f.write(f"{event}: {len(rows)} participants\n")
        f.write(f"Errors: {len(errors)}\n")
    with open("error_log.txt", "w", encoding="utf-8") as f:
        for item in errors: f.write(" | ".join(map(str, item)) + "\n")

if __name__ == "__main__":
    paths = [f"department{i}.txt" for i in range(1, 6)]
    master, events, errors = process_files(paths)
    write_outputs(master, events, errors)
    print(f"Accepted: {len(master)}")
    print(f"Events: {len(events)}")
    print(f"Errors: {len(errors)}")
