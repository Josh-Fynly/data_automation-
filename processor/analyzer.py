import pandas as pd

def analyze_data(df: pd.DataFrame) -> dict:
    summary = {}

    numeric_cols = df.select_dtypes(include=['number']).columns

    for column in numeric_cols:
        summary[column] = {
            "mean": float(df[column].mean()),
            "sum": float(df[column].sum()),
            "max": float(df[column].max()),
            "min": float(df[column].min()),
        }

    return summary
