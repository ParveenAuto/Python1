import os
import pandas as pd

# Give file path here
file_path = "/Users/pd/Desktop/python/RES4CITY_Project/RES4CITY_Analytics_Live_data_set_170225.xlsx"

# File check 
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Error: File not found at {file_path}")

# Data from excel
columns_to_extract = {
    "Users_Info": ["user_id", "country", "date_joined"],
    "MC_Enrolment_Info": ["user_id", "course_id", "enrolment_date"],
    "MC_Certificates": ["user_id", "course_id", "grade", "date_earned"],
}

# Read Excel
xls = pd.ExcelFile(file_path)

# Extract required columns from each sheet
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

# Add 'date_joined' and 'country' from 'Users_Info' based on 'user_id'
if "Users_Info" in data_frames:
    merged_df = merged_df.merge(data_frames["Users_Info"], on="user_id", how="left")

# Add 'grade' and 'date_earned' from 'MC_Certificates' based on 'user_id' and 'course_id'
if "MC_Certificates" in data_frames:
    merged_df = merged_df.merge(data_frames["MC_Certificates"], on=["user_id", "course_id"], how="left")
    
    # Drop duplicate 'date_earned' values, keeping only the first occurrence
    merged_df = merged_df.drop_duplicates(subset=["user_id", "course_id", "grade"], keep='first')

# Remove duplicate entries based on all columns except 'date_earned'
merged_df = merged_df.drop_duplicates(subset=[col for col in merged_df.columns if col != "date_earned"], keep='first')

# Perform splitting after merging all data
# Split date and time into separate columns
for col in ["date_joined", "enrolment_date", "date_earned"]:
    if col in merged_df.columns:
        merged_df[col] = pd.to_datetime(merged_df[col], errors='coerce')
        merged_df[f"{col}_date"] = merged_df[col].dt.date
        merged_df[f"{col}_time"] = merged_df[col].dt.time
        merged_df.drop(columns=[col], inplace=True)  # Remove original column

# Split course_id into course_id, organisation, and course_number
if "course_id" in merged_df.columns:
    split_course = merged_df["course_id"].str.split("[:+]", expand=True)
    merged_df["course_id"] = split_course[0]  # First split (before ':')
    merged_df["organisation"] = split_course[1]  # Second split (first '+')
    merged_df["course_number"] = split_course[2]  # Keep only the main course number

# Write to a new sheet inside the same Excel file
with pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    merged_df.to_excel(writer, sheet_name="final_data", index=False)

print("Data successfully merged using MC_Enrolment_Info as the base file, with unique user_id and saved to 'final_data'")

# ---- Add Enrolment Trend Analysis ----

# Ensure 'enrolment_date_date' is in datetime format
merged_df['enrolment_date_date'] = pd.to_datetime(merged_df['enrolment_date_date'], errors='coerce')

# Extract Year-Month for grouping
merged_df['Year-Month'] = merged_df['enrolment_date_date'].dt.to_period('M')

# Count enrolments per month
monthly_enrolments = merged_df.groupby('Year-Month').size()

# Plot the trend
plt.figure(figsize=(10, 5))
plt.plot(monthly_enrolments.index.astype(str), monthly_enrolments.values, marker='o', linestyle='-', color='b')

# Formatting
plt.xlabel("Month")
plt.ylabel("Number of Enrolments")
plt.title("Monthly Enrolment Trend")
plt.xticks(rotation=45)  # Rotate x-axis labels
plt.grid(True)

# Show plot
plt.show()