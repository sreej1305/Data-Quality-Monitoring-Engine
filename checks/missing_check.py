def check_missing_values(df):
    """Core data-quality responsibility: detect missing values."""
    return df.isnull().sum().to_dict()
