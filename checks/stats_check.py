def statistical_checks(df):
    """Detects anomalies & unexpected distributions."""
    return {
        "row_count": len(df),
        "duplicate_rows": int(df.duplicated().sum()),
        "numeric_summary": df.describe().to_dict()
    }
