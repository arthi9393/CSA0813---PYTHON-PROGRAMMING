# CSA08 – Python Programming – Assignment 1
## Ksheera Village Milk Co-operative Payment Calculator

**Student name:** ARTHI A 
**Register number:** 192525152
**Course:** CSA08 – Python Programming  
**Python version:** Python 3.10+ (tested with the installed version on your computer; record your exact `py --version`)  
**GitHub repository:** `CSA08-<RegisterNumber>-Assignment1`

### Project overview
A modular payment calculator for milk quantity, fat percentage and SNF percentage. It uses `Decimal` for paisa-accurate money calculations, validates entries, applies a reusable rate card and supports the April–June seasonal rate and volume bonus.

### Files
- `milkrate.py` – constants, validation, calculation functions and seasonal rate selection.
- `main.py` – interactive data-entry script.
- `test_milkrate.py` – repeatable assertion-based tests.
- `benchmark.py` – float/Decimal timing comparison.
- `Task02/complete_decimal.py` – completed Decimal TODO program.
- `Task07/test_import.py` – demonstrates importing the module.
- `Task12/design_challenge.py` – seasonal-rate and bonus demonstration.
- `Task01` … `Task12` – task notes and screenshot folders.

### Run commands (Windows PowerShell)
```powershell
py --version
py milkrate.py
py main.py
py test_milkrate.py
py benchmark.py
py Task02/complete_decimal.py
py Task07/test_import.py
py Task12/design_challenge.py
```
Run commands from the repository root so Python can find `milkrate.py`.

### Libraries
Only Python standard-library modules are used: `decimal`, `time`, and built-in language features. No external packages are required. `requirements.txt` is included.

### Results
- Standard milk (3.5% fat, 8.5% SNF): Rs 30.00/L.
- 8.5 L at 4.2% fat and 8.7% SNF: Rs 283.90.
- 12 L at 3.1% fat and 8.3% SNF: Rs 333.60.
- Automated tests cover normal, boundary, invalid, seasonal and bonus cases.

### Screenshots
Add your own screenshots to the relevant `TaskXX/screenshots/` folders and the root `screenshots/` folder. Do not use sample or fabricated screenshots; capture your own execution.

### GitHub submission
Create a repository named `CSA08-<RegisterNumber>-Assignment1`. Upload this folder structure, commit progressively (at least one meaningful commit per task), and share the repository with the faculty. Replace all square-bracket placeholders before submission.
