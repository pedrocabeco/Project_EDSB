# src/convert_to_csv.py

from pathlib import Path
import pandas as pd

# 1️⃣ Folder where your Excel files are
DATA_RAW = Path("data/raw")

# 2️⃣ Go through each .xlsx file in that folder
for xlsx_file in DATA_RAW.glob("*.xlsx"):
    print(f"Converting {xlsx_file.name} ...")

    # 3️⃣ Read the Excel file
    df = pd.read_excel(xlsx_file, engine="openpyxl")

    # 4️⃣ Save it as a CSV with the same name
    csv_file = xlsx_file.with_suffix(".csv")
    df.to_csv(csv_file, index=False)

    print(f"✅ Saved as {csv_file.name}")