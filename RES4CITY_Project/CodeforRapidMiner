# Import required libraries
import pandas as pd

#  Load the Excel file
file_path = "/Users/pd/Desktop/python/RES4CITY_Project/RES4CITY_Analytics_Live_data_set_170225.xlsx"
xls = pd.ExcelFile(file_path)

# Load relevant sheets
final_data_df = xls.parse("final_data")  # Already cleaned data
courseware_df = xls.parse("Courseware_Module")  # Contains module interactions

# Step 1: Extract Course Number from Courseware_Module
# The course_id format is "course-v1:UPV+MC17v1+2024_01", so extract "MC17v1"
courseware_df['course_number'] = courseware_df['course_id'].str.extract(r'(\bMC\d+v\d+\b)')

# Step 2: Count Modules Attempted Per User Per Course
# Count occurrences of course_number per user
modules_attempted_fixed = courseware_df.groupby(['user_id', 'course_number']).size().reset_index(name='modules_attempted')

# Step 3: Merge This Count Into Final Data
final_data_fixed = final_data_df.merge(modules_attempted_fixed, on=['user_id', 'course_number'], how="left")

# Fill missing values for modules_attempted (users with no module interactions get 0)
final_data_fixed['modules_attempted'].fillna(0, inplace=True)

# Convert modules_attempted to integer
final_data_fixed['modules_attempted'] = final_data_fixed['modules_attempted'].astype(int)

# Step 4: Ensure Grades Are Taken Directly from Final Data
final_data_fixed['grade'] = pd.to_numeric(final_data_fixed['grade'], errors='coerce')

# Fill missing grades with 0 (assuming dropouts have no recorded grade)
final_data_fixed['grade'].fillna(0, inplace=True)

# Step 5: Save the Processed Dataset to CSV
output_csv = "/Users/pd/Desktop/python/RES4CITY_Project/final_data_with_simplified_modules_attempted.csv"
final_data_fixed.to_csv(output_csv, index=False)

print(f"Processed dataset saved as '{output_csv}'")