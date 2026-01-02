def validate_schema(df, schema):
    """Detects missing or unexpected columns."""
    issues = []
    for column, dtype in schema.items():
        if column not in df.columns:
            issues.append(f"Missing column: {column}")
    return issues
