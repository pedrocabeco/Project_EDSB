from pathlib import Path
import pandas as pd

# Define the folder where the Excel files are
DATA_RAW = Path("data/raw")

# Loop through each .xlsx file in that folder
for xlsx_file in DATA_RAW.glob("*.xlsx"):
    # Read the Excel file using the openpyxl engine
    df = pd.read_excel(xlsx_file, engine="openpyxl")

    # Save it as a CSV with the same name
    csv_file = xlsx_file.with_suffix(".csv")
    df.to_csv(csv_file, index=False)

    print(f"Converted: {xlsx_file.name} → {csv_file.name}")