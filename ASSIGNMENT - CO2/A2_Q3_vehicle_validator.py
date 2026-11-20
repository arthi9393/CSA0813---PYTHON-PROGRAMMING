def normalise(text):
    return text.strip().replace(" ", "").replace("-", "").upper()

def is_valid(reg):
    if len(reg) not in (9, 10):
        return False
    series_length = len(reg) - 8
    return (reg[:2].isalpha() and reg[2:4].isdigit()
            and reg[4:4+series_length].isalpha()
            and reg[4+series_length:].isdigit())

def format_number(reg):
    if not is_valid(reg):
        return "INVALID"
    n = normalise(reg)
    return f"{n[:2]} {n[2:4]} {n[4:-4]} {n[-4:]}"

tests = ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234",
         "TN 22 1234 AB", "MH 12 CD 4567", "ab-99-z-0001"]
for raw in tests:
    reg = normalise(raw)
    print(f"{raw:16} -> {reg:11} {'valid' if is_valid(reg) else 'INVALID'}")
print("Receipt:", format_number("tn 09 ab 1234"))
