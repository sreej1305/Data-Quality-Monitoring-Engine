# Data Quality Monitoring Engine

The **Data Quality Monitoring Engine** is a Python system that validates data against schemas to detect issues and missing values. 
It generates structured reports and logs to ensure data integrity for downstream ML and analytics pipelines.

## 📁 Project Structure

```text
data_quality_engine/
├── data/                     # Input datasets (CSV/JSON)
├── schemas/                  # Expected data definitions
├── checks/                   # Modular quality checks
├── reports/                  # Generated quality reports
├── logs/                     # Detailed engine logs
├── engine.py                 # Main orchestrator
└── requirements.txt          # Dependencies
```

## 🚀 How to Run

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Engine**:
   ```bash
   python engine.py
   ```

3. **View Results**:
   - Quality Report: `reports/quality_report.txt`
   - Logs: `logs/engine.log`

## 🧩 Key Features

- **Schema Validation**: Detects missing or unexpected columns.
- **Missing Value Detection**: Identifies `null` values across all columns.
- **Statistical Checks**: Calculates row counts, duplicates, and numeric summaries.
- **Enterprise Logging**: Maintains detailed logs of every execution step.
