Here's a Python script that reads an Excel file from /myFolder, extracts specific columns from different sheets, and writes them into a new sheet (newSheet) in the same file.

Steps the script follows:

1. Load the Excel file from /myFolder.


2. Extract specified columns from multiple sheets.


3. Combine them into a new DataFrame.


4. Write the extracted data into a new sheet (newSheet) in the same file.




---

Python Script:

import pandas as pd

# Define file path
file_path = "/myFolder/my_excel_file.xlsx"

# Define columns to extract (sheet_name: [columns])
columns_to_extract = {
    "Sheet1": ["Column1", "Column2"],
    "Sheet2": ["Column3"],
    # Add more sheets and columns as needed
}

# Read the Excel file
xls = pd.ExcelFile(file_path)

# Extract required columns from each sheet
data_frames = []
for sheet, cols in columns_to_extract.items():
    if sheet in xls.sheet_names:  # Check if sheet exists
        df = pd.read_excel(xls, sheet_name=sheet, usecols=cols)
        data_frames.append(df)

# Combine extracted columns into a single DataFrame
merged_df = pd.concat(data_frames, axis=1)

# Write to a new sheet inside the same Excel file
with pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    merged_df.to_excel(writer, sheet_name="newSheet", index=False)

print("Data successfully extracted and written to 'newSheet' inside the Excel file.")


---

How to Use the Script:

1. Modify file_path to your actual Excel file path.


2. Update columns_to_extract dictionary with your required sheets and column names.


3. Run the script, and it will create/update the newSheet with selected columns.




---

Requirements:

Ensure you have the required libraries installed:

pip install pandas openpyxl

Let me know if you need any modifications!
