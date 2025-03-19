import pandas as pd
import joblib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the trained model
model = joblib.load("/Users/pd/Desktop/python/dropout_prediction_model.pkl")

# Load new students' early engagement data
new_students = pd.read_csv("/Users/pd/Desktop/python/RES4CITY_Project/future_students_sample.csv")

# Convert `grade` from percentage string to float
if "grade" in new_students.columns:
    new_students["grade"] = new_students["grade"].str.replace('%', '', regex=True).astype(float)

# Convert date columns to datetime
new_students["enrolment-date"] = pd.to_datetime(new_students["enrolment-date"], errors="coerce")
new_students["date_joined"] = pd.to_datetime(new_students["date_joined"], errors="coerce")

# Calculate days since enrollment & days since joining
new_students["days_since_enrollment"] = (pd.to_datetime("today") - new_students["enrolment-date"]).dt.days
new_students["days_since_joined"] = (pd.to_datetime("today") - new_students["date_joined"]).dt.days

# Fill missing values
new_students["days_since_enrollment"].fillna(new_students["days_since_enrollment"].median(), inplace=True)
new_students["days_since_joined"].fillna(new_students["days_since_joined"].median(), inplace=True)

# Load the feature names used during training
training_features = joblib.load("/Users/pd/Desktop/python/model_features.pkl")  # This file must be saved during training

# Ensure feature alignment (Fixing the column mismatch error)
# Step 1: Add missing columns (fill with 0)
for col in training_features:
    if col not in new_students.columns:
        new_students[col] = 0  # Fill missing categorical columns with 0

# Step 2: Keep only the training columns (drop anything extra)
X_new = new_students[training_features]

# Predict dropout probabilities
dropout_probabilities = model.predict_proba(X_new)[:, 1]

# Add predictions to the dataset
new_students["predicted_dropout_prob"] = dropout_probabilities

# Save predictions
new_students.to_csv("dropout_predictions_fixed.csv", index=False)
print("Predictions saved as 'dropout_predictions_fixed.csv'")

# Display top at-risk students
print(new_students.sort_values(by="predicted_dropout_prob", ascending=False).head(10))

# Plot Dropout Probability Distribution
plt.figure(figsize=(10, 5))
sns.histplot(dropout_probabilities, bins=20, kde=True, color="red")
plt.title("Dropout Probability Distribution")
plt.xlabel("Predicted Dropout Probability")
plt.ylabel("Count")
plt.show()