import pandas as pd
from src.etl import transform


def test_transform_removes_missing_salary():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "department": ["engineering", "marketing", "sales"],
        "salary": [100000, None, 90000]
    })
    transformed_df = transform(df)

    assert transformed_df["salary"].isnull().sum() == 0
    assert len(transformed_df) == 2  # Charlie is kept, Bob is removed


def test_transform_department_uppercase():
    df = pd.DataFrame({
        "name": ["Alice"],
        "department": ["engineering"],
        "salary": [100000]
    })
    transformed_df = transform(df)
    assert transformed_df.loc[0, "department"] == "ENGINEERING"


def test_transform_salary_with_bonus():
    df = pd.DataFrame({
        "name": ["Alice"],
        "department": ["engineering"],
        "salary": [100000]
    })
    transformed_df = transform(df)
    assert transformed_df.loc[0, "salary_with_bonus"] == 110000
