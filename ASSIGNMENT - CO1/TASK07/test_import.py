import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import milkrate as mr
print("Imported payout:", mr.payout("8.5", "4.2", "8.7"))
