import logging
import json
import pandas as pd
import os
from checks.schema_check import validate_schema
from checks.missing_check import check_missing_values
from checks.stats_check import statistical_checks

# Ensure directories exist
os.makedirs("logs", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Setup Logging
logging.basicConfig(
    filename="logs/engine.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"
)

def load_data(path):
    logging.info(f"Loading dataset from {path}")
    try:
        return pd.read_csv(path)
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        raise

def run_engine():
    logging.info("Starting Data Quality Engine")
    
    # Configuration
    data_path = "data/sample_data.csv"
    schema_path = "schemas/schema.json"
    report_path = "reports/quality_report.txt"
    
    # Load Data
    df = load_data(data_path)
    
    # Load Schema
    with open(schema_path) as f:
        schema = json.load(f)
    
    # Execute Quality Checks
    logging.info("Executing Schema Validation")
    schema_issues = validate_schema(df, schema)
    
    logging.info("Executing Missing Value Check")
    missing_issues = check_missing_values(df)
    
    logging.info("Executing Statistical Checks")
    stats = statistical_checks(df)
    
    # Generate Report
    logging.info(f"Generating report at {report_path}")
    with open(report_path, "w") as report:
        report.write("===============================\n")
        report.write("DATA QUALITY REPORT\n")
        report.write("===============================\n\n")
        
        report.write("--- Schema Issues ---\n")
        if schema_issues:
            for issue in schema_issues:
                report.write(f"- {issue}\n")
        else:
            report.write("No schema issues detected.\n")
        report.write("\n")
        
        report.write("--- Missing Values ---\n")
        for col, count in missing_issues.items():
            report.write(f"{col}: {count}\n")
        report.write("\n")
        
        report.write("--- Statistics ---\n")
        report.write(f"Total Rows: {stats['row_count']}\n")
        report.write(f"Duplicate Rows: {stats['duplicate_rows']}\n")
        report.write("\nNumeric Summary:\n")
        report.write(json.dumps(stats['numeric_summary'], indent=2))
        report.write("\n")

    logging.info("Data Quality Engine completed successfully")

if __name__ == "__main__":
    run_engine()
