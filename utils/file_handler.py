import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except Exception as e:
        raise Exception(f"Error loading CSV: {e}")

def save_csv(df: pd.DataFrame, path: str):
    try:
        df.to_csv(path, index=False)
    except Exception as e:
        raise Exception(f"Error saving CSV: {e}")
