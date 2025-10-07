import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split

print("✅ All libraries imported successfully!")
print("all set and ready to go!")

DATA_RAW = Path(__file__).resolve().parents[1] / "data" / "raw"

df = pd.read_excel(DATA_RAW / "Telco_customer_churn_demographics.xlsx")
print(df.head())