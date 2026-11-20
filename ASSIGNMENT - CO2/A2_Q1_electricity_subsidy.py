def separate_ifs(units, ration_card, elderly):
    decisions = []
    if units <= 100:
        decisions.append("Full subsidy")
    if 101 <= units <= 200 and ration_card:
        decisions.append("Partial subsidy")
    if units > 200 and elderly:
        decisions.append("Special subsidy")
    if not decisions:
        decisions.append("No subsidy")
    return decisions

def elif_rule(units, ration_card, elderly):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200 and ration_card:
        return "Partial subsidy"
    elif units > 200 and elderly:
        return "Special subsidy"
    else:
        return "No subsidy"

households = [
    (100, False, False), (101, True, False), (101, False, False),
    (150, True, False), (200, True, False), (201, False, True),
    (201, False, False), (250, True, True)
]
print("UNITS  RATION  ELDERLY  SEPARATE IF                         IF-ELIF-ELSE")
for u, r, e in households:
    print(f"{u:<6}  {str(r):<6}  {str(e):<7}  {', '.join(separate_ifs(u,r,e)):<35} {elif_rule(u,r,e)}")
print("\nDecision: if-elif-else guarantees one mutually exclusive result.")
