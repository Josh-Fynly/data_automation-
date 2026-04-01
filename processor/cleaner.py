import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna(method="ffill")

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    return df
