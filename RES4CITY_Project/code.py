import os
import pandas as pd

# File path
file_path = "/Users/pd/Desktop/python/RES4CITY_Project/RES4CITY_Analytics_Live_data_set_170225.xlsx"

# Check if file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Error: File not found at {file_path}")

# Columns to extract from each sheet
columns_to_extract = {
    "Users_Info": ["user_id", "country", "date_joined"],
    "MC_Enrolment_Info": ["user_id", "course_id", "enrolment_date"],
    "MC_Certificates": ["user_id", "course_id", "grade", "date_earned"],
}

# Read the Excel file
xls = pd.ExcelFile(file_path)

# Extract required columns
data_frames = {}
for sheet, cols in columns_to_extract.items():
    if sheet in xls.sheet_names:  # Check if sheet exists
        df = pd.read_excel(xls, sheet_name=sheet, usecols=cols)
        data_frames[sheet] = df
    else:
        print(f"Warning: Sheet '{sheet}' not found in the Excel file.")

# Ensure MC_Enrolment_Info is the base DataFrame
if "MC_Enrolment_Info" not in data_frames:
    raise ValueError("MC_Enrolment_Info sheet is required but not found.")

merged_df = data_frames["MC_Enrolment_Info"].copy()

# Merge 'Users_Info' to get 'date_joined' and 'country'
if "Users_Info" in data_frames:
    merged_df = merged_df.merge(data_frames["Users_Info"], on="user_id", how="left")

# Merge 'MC_Certificates' to get 'grade' and 'date_earned'
if "MC_Certificates" in data_frames:
    merged_df = merged_df.merge(data_frames["MC_Certificates"], on=["user_id", "course_id"], how="left")
    merged_df = merged_df.drop_duplicates(subset=["user_id", "course_id", "grade"], keep='first')

# Remove duplicate entries based on all columns except 'date_earned'
merged_df = merged_df.drop_duplicates(subset=[col for col in merged_df.columns if col != "date_earned"], keep='first')

# Convert date columns to datetime format (keeps original format)
for col in ["date_joined", "enrolment_date", "date_earned"]:
    if col in merged_df.columns:
        merged_df[col] = pd.to_datetime(merged_df[col], errors='coerce')


# Extract date (overwrite the original column) and time (create a new column)
for col in ["date_joined", "enrolment_date", "date_earned"]:
    if col in merged_df.columns:
        merged_df[f"{col}_time"] = merged_df[col].dt.strftime('%H:%M:%S')  # Create a new column for time
        merged_df[col] = merged_df[col].dt.date  # Overwrite original column with only the date



# Rename columns
column_rename_map = {
    "date_joined": "date_joined",
    "date_joined_time": "joined_time",
    "enrolment_date": "enrolment-date",
    "enrolment_date_time": "enrolment_time",
    "date_earned": "date_earned",
    "date_earned_time": "earned_time",
}

merged_df.rename(columns=column_rename_map, inplace=True)

# Split course_id into course_id, organisation, and course_number
if "course_id" in merged_df.columns:
    split_course = merged_df["course_id"].str.split("[:+]", expand=True)
    merged_df["course_id"] = split_course[0]  # First split (before ':')
    merged_df["organisation"] = split_course[1]  # Second split (first '+')
    merged_df["course_number"] = split_course[2]  # Keep only the main course number
    
    
# Define the desired column order
desired_column_order = [
    "user_id", "country", "course_id", "date_joined", "joined_time",
    "enrolment-date", "enrolment_time", "organisation", "course_number",
    "grade", "date_earned", "earned_time"
]

# Reorder columns
merged_df = merged_df[desired_column_order]

# Drop the course_id column
merged_df.drop(columns=["course_id"], inplace=True)


# # Define new file path
new_file_path = "/Users/pd/Desktop/python/RES4CITY_Project/Cleaned_data.xlsx"


#  Save to a new file
merged_df.to_excel(new_file_path, sheet_name="Cleaned_Data", index=False, engine="openpyxl")

#  Update 'final_data' in the original file
with pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    merged_df.to_excel(writer, sheet_name="final_data", index=False)

print(f" Data successfully saved in:\n {new_file_path} (New file)\n {file_path} (Updated 'final_data' sheet)")
