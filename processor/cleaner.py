import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()

    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col] = df[col].fillna(df[col].mean())

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna(method="ffill")

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    return df
