import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from milkrate import seasonal_payout, volume_bonus, final_ten_day_payment
from decimal import Decimal

print("Regular:", seasonal_payout("10", "4.26", "8.76", "regular"))
print("April-June:", seasonal_payout("10", "4.26", "8.76", "summer"))
print("Bonus for 501 L:", volume_bonus("501"))
farmer_entries = [{"litres": "251", "fat": "4.26", "snf": "8.76"},
                  {"litres": "250", "fat": "4.26", "snf": "8.76"}]
print("Ten-day payment incl. bonus:",
      final_ten_day_payment(farmer_entries, "summer"))
