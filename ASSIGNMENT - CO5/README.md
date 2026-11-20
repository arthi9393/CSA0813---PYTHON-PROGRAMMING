# CSA08 – PYTHON PROGRAMMING
## ASSIGNMENT 5 – CO5
### DATA ACQUISITION, CLEANING, ANALYSIS AND AI APPLICATIONS

**Student Name:** ARTHI A
**Register Number:** 192525152
**Course Code:** CSA08  
**Assignment:** Assignment 5 – CO5  
**Python Version:** Python 3.12  


---

## 1. Introduction

This assignment focuses on acquiring, cleaning, storing, analysing and visualising air-quality data using Python. It also introduces basic AI applications such as sentiment analysis, text summarisation and a rule-based chatbot.

The case study is based on a City Air-Quality Monitoring Network containing readings from multiple monitoring stations.

## 2. Software and Libraries Used

- Python 3.12
- SQLite3
- CSV
- Pandas
- Matplotlib
- Statistics
- Regular Expressions (re)
- Time and cProfile

## 3. Installation

Install the required libraries using:

```bash
python -m pip install -r requirements.txt
```

## 4. Task Description and Execution

### Task 01 – Data Cleaning and Normalisation
**File:** `Task01.py`

- Reads air-quality readings.
- Handles missing and invalid values.
- Removes duplicate records.
- Converts Fahrenheit into Celsius.
- Stores cleaned data in SQLite.
- Performs SQL queries.
- Generates charts using Matplotlib.

**Run command:**
```bash
python Task01.py
```

### Task 02 – Adversarial Data Testing
**File:** `Task02.py`

- Tests missing CSV columns.
- Tests incorrect delimiters and empty files.
- Demonstrates SQL parameterised queries.
- Explains SQL injection prevention.

**Run command:**
```bash
python Task02.py
```

### Task 03 – Loops vs Libraries vs SQL
**File:** `Task03.py`

- Generates datasets for 1, 12 and 120 stations.
- Compares Python aggregation, Pandas and SQL.
- Measures execution time.
- Uses cProfile for performance analysis.

**Run command:**
```bash
python Task03.py
```

### Task 04 – Sentiment Analysis and Final Engineering Decision
**File:** `Task04.py`

- Implements a lexicon-based sentiment analyser.
- Handles simple negation.
- Generates an extractive text summary.
- Measures sentiment agreement.
- Tests SQLite indexing performance.

**Run command:**
```bash
python Task04.py
```

## 5. Output Files

The programs generate the following output files:

- `air_quality.db` – SQLite database.
- `pm25_trend.png` – PM2.5 trend chart.
- `station_comparison.png` – Station comparison chart.
- `temperature_vs_pm25.png` – Temperature and PM2.5 relationship.
- `pm25_distribution.png` – PM2.5 distribution chart.
- `benchmark_1.csv`, `benchmark_12.csv`, `benchmark_120.csv` – Generated datasets.
- `profile.stats` – Profiling information.

## 6. Learning Outcomes

Through this assignment, I learned:

1. How to acquire and clean CSV data using Python.
2. How to store and retrieve data using SQLite.
3. How to perform data normalisation.
4. How to visualise data using Matplotlib.
5. How to compare Python loops, Pandas and SQL.
6. How to debug and profile Python programs.
7. How to implement basic sentiment analysis and text summarisation.
8. How to improve database query performance using indexing.

## 7. Conclusion

This assignment helped me understand the complete data-processing workflow: acquiring, inspecting, cleaning, normalising, storing, querying, visualising and analysing data. It also provided practical experience with introductory AI applications and performance evaluation using Python.

---

**Note:** All programs must be executed individually. Actual execution screenshots and measured timings should be added to the GitHub repository before submission.
