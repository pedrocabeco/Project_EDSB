# src/main.py
from pathlib import Path           # handles folders/paths safely
import pandas as pd                # tables library

RAW = Path("data/raw")             # folder where your CSVs live

# 1) Load ONE file
df = pd.read_csv(RAW / "Telco_customer_churn_demographics.csv")

# 2) Show a tiny preview
print("Rows x Cols:", df.shape)
print(df.head(3))

files = {
    "dem": "Telco_customer_churn_demographics.csv",
    "loc": "Telco_customer_churn_location.csv",
    "pop": "Telco_customer_churn_population.csv",
    "svc": "Telco_customer_churn_services.csv",
    "sts": "Telco_customer_churn_status.csv",
}

tables = {k: pd.read_csv(RAW / v) for k, v in files.items()}
for name, t in tables.items():
    print(name, t.shape)

def clean_cols(df):
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(r"\s+", "_", regex=True)
        .str.replace(r"[^0-9a-zA-Z_]+", "", regex=True)
        .str.lower()
    )
    return df