def analyze_data(df):
    summary = {}

    for column in df.select_dtypes(include=['int64', 'float64']).columns:
        summary[column] = {
            "mean": df[column].mean(),
            "sum": df[column].sum(),
            "max": df[column].max(),
            "min": df[column].min(),
        }

    return summary
