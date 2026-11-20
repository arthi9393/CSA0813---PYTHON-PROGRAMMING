"""Q7 - Merge contacts by normalized phone number."""
import random
import re
import time

def normalize_phone(phone):
    if not phone:
        return ""
    digits = re.sub(r"\D", "", phone)
    # For this sample, remove India's country prefix when a 12-digit number starts 91.
    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]
    return digits

def merge_contacts(contact_lists):
    merged = {}
    for contacts in contact_lists:
        for contact in contacts:
            name = (contact.get("name") or "Unknown").strip()
            phone = normalize_phone(contact.get("phone", ""))
            email = (contact.get("email") or "").strip().lower()
            if not phone:
                # Missing phone cannot safely identify a person; keep a unique record.
                key = f"no-phone-{len(merged)}"
            else:
                key = phone
            if key not in merged:
                merged[key] = {"name": name, "numbers": set(), "emails": set()}
            if name != "Unknown" and merged[key]["name"] == "Unknown":
                merged[key]["name"] = name
            if contact.get("phone"):
                merged[key]["numbers"].add(contact["phone"].strip())
            if email:
                merged[key]["emails"].add(email)
    return merged

def benchmark():
    print("Contacts, dictionary_merge_seconds")
    for n in (1_000, 100_000):
        contacts = [[{"name": f"Person {i}", "phone": f"+91 90000 {i:05d}",
                      "email": f"p{i}@example.com"} for i in range(n)]]
        start = time.perf_counter(); merged = merge_contacts(contacts)
        print(n, f"{time.perf_counter()-start:.6f}", "unique:", len(merged))

def main():
    phone_a = [
        {"name": "Dr. Ravi", "phone": "+91 98400 12345", "email": "RAVI@MAIL.COM"},
        {"name": "Meena", "phone": "98765 43210", "email": "meena@mail.com"},
    ]
    phone_b = [
        {"name": "Ravi Kumar", "phone": "9840012345", "email": "ravi.work@mail.com"},
        {"name": "Meena", "phone": " +91-98765-43210 ", "email": ""},
        {"name": "No phone contact", "phone": "", "email": "unknown@mail.com"},
    ]
    result = merge_contacts([phone_a, phone_b])
    for key, value in result.items():
        print(key, "=>", value)
    assert len(result) == 3
    print("Ravi normalized key:", normalize_phone("+91 98400 12345"))
    benchmark()

if __name__ == "__main__":
    main()
