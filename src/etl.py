import pandas as pd

def extract(csv_path: str) -> pd.DataFrame:
    """Extract data from CSV into a pandas DataFrame."""
    return pd.read_csv(csv_path)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform data:
    - Remove rows with missing 'salary'
    - Convert 'department' to uppercase
    - Add 10% bonus to salary
    """
    df = df.dropna(subset=["salary"])
    df["department"] = df["department"].str.upper()
    df["salary_with_bonus"] = df["salary"] * 1.1
    return df

def load(df: pd.DataFrame, out_path: str) -> None:
    """Load transformed data to CSV."""
    df.to_csv(out_path, index=False)

if __name__ == "__main__":
    data = extract("/sample_unittesting/sample_data.csv")
    transformed = transform(data)
    load(transformed, "/sample_unittesting/output.csv")
