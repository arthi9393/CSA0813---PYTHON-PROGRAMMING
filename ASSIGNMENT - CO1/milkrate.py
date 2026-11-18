"""Ksheera Village Milk Co-operative payment calculation module."""
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
STEP_SIZE = Decimal("0.1")
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")
MIN_SNF = Decimal("0.0")
MAX_SNF = Decimal("15.0")

def D(value):
    """Convert user data to Decimal through text to avoid binary float artefacts."""
    return value if isinstance(value, Decimal) else Decimal(str(value))

def whole_steps(reading, standard):
    """Return nearest 0.1-percentage-point step, using half-up rounding."""
    return int(((D(reading) - D(standard)) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP))

def validate_entry(farmer_id, litres, fat, snf, shift):
    """Raise ValueError when an entry violates the co-operative's input rules."""
    q, f, s = D(litres), D(fat), D(snf)
    if not str(farmer_id).strip():
        raise ValueError("Farmer ID cannot be empty")
    if q <= 0:
        raise ValueError("Litres must be greater than zero")
    if not (MIN_FAT <= f <= MAX_FAT):
        raise ValueError(f"Fat must be between {MIN_FAT} and {MAX_FAT}%")
    if not (MIN_SNF <= s <= MAX_SNF):
        raise ValueError(f"SNF must be between {MIN_SNF} and {MAX_SNF}%")
    if shift not in ("M", "E"):
        raise ValueError("Shift must be M (morning) or E (evening)")
    return True

def rate_per_litre(fat, snf, rate_card=None):
    """Calculate the per-litre rate using the supplied or standard rate card."""
    card = rate_card or {
        "base": BASE_RATE, "fat_step": FAT_STEP_VALUE,
        "snf_step": SNF_STEP_VALUE, "standard_fat": STANDARD_FAT,
        "standard_snf": STANDARD_SNF
    }
    fat_steps = whole_steps(fat, card["standard_fat"])
    snf_steps = whole_steps(snf, card["standard_snf"])
    rate = (D(card["base"]) + fat_steps * D(card["fat_step"])
            + snf_steps * D(card["snf_step"]))
    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def payout(litres, fat, snf, rate_card=None):
    """Return one farmer's payment rounded to the nearest paisa."""
    amount = D(litres) * rate_per_litre(fat, snf, rate_card)
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def ten_day_total(entries):
    """Return the sum of already validated entry payments as an exact Decimal."""
    return sum((payout(e["litres"], e["fat"], e["snf"]) for e in entries),
               Decimal("0.00")).quantize(Decimal("0.01"))

def read_rate_card(season="regular"):
    """Return a seasonal rate card; April-June uses the announced seasonal rates."""
    if season.lower() in ("april-june", "summer"):
        return {
            "base": Decimal("32.00"), "fat_step": Decimal("0.45"),
            "snf_step": Decimal("0.30"), "standard_fat": STANDARD_FAT,
            "standard_snf": STANDARD_SNF
        }
    return {
        "base": BASE_RATE, "fat_step": FAT_STEP_VALUE,
        "snf_step": SNF_STEP_VALUE, "standard_fat": STANDARD_FAT,
        "standard_snf": STANDARD_SNF
    }

def seasonal_payout(litres, fat, snf, season="regular"):
    """Calculate payment with the selected seasonal rate card."""
    return payout(litres, fat, snf, read_rate_card(season))

def volume_bonus(total_litres):
    """Return Rs 0.50 per litre only when ten-day volume exceeds 500 litres."""
    q = D(total_litres)
    if q > Decimal("500"):
        return (q * Decimal("0.50")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Decimal("0.00")

def final_ten_day_payment(entries, season="regular"):
    """Return milk payment plus eligible volume bonus for one farmer."""
    milk_total = sum((seasonal_payout(e["litres"], e["fat"], e["snf"], season)
                      for e in entries), Decimal("0.00"))
    litres_total = sum((D(e["litres"]) for e in entries), Decimal("0.00"))
    return (milk_total + volume_bonus(litres_total)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    samples = [(10, "3.5", "8.5"), ("8.5", "4.2", "8.7"),
               (12, "3.1", "8.3")]
    for litres, fat, snf in samples:
        rate = rate_per_litre(fat, snf)
        print(f"{str(litres):>5} L fat {fat} snf {snf} "
              f"rate {rate:>6.2f} pay {payout(litres, fat, snf):>8.2f}")
