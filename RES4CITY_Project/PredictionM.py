
import pandas as pd
import numpy as np
import joblib

# Step 1: Load the trained model and scaler
model = joblib.load("/Users/pd/Desktop/python/model_random_forest.pkl")
scaler = joblib.load("/Users/pd/Desktop/python/dropout_scaler.pkl")

# Step 2: Load new student data
new_students = pd.read_csv("/Users/pd/Desktop/python/RES4CITY_Project/future_students_sample.csv")

# Step 3: Date preprocessing
new_students["enrolment-date"] = pd.to_datetime(new_students["enrolment-date"], errors="coerce")
new_students["date_joined"] = pd.to_datetime(new_students["date_joined"], errors="coerce")
if "date_earned" in new_students.columns:
    new_students["date_earned"] = pd.to_datetime(new_students["date_earned"], errors="coerce")
    new_students["earned_flag"] = new_students["date_earned"].notna().astype(int)
else:
    new_students["earned_flag"] = 0

# Step 4: Feature Engineering
new_students["days_to_enroll"] = (new_students["enrolment-date"] - new_students["date_joined"]).dt.days
new_students["week_enrolled"] = new_students["enrolment-date"].dt.weekday
new_students["joined_hour"] = pd.to_datetime(new_students["joined_time"], errors="coerce").dt.hour
new_students["days_since_enroll"] = (pd.Timestamp.now() - new_students["enrolment-date"]).dt.days

# Fill missing engineered features
new_students.fillna({
    "days_to_enroll": new_students["days_to_enroll"].median(),
    "week_enrolled": new_students["week_enrolled"].mode()[0],
    "joined_hour": new_students["joined_hour"].mode()[0],
    "days_since_enroll": new_students["days_since_enroll"].median()
}, inplace=True)

# Step 5: Prepare features with correct alignment
X_new = new_students.select_dtypes(include=[np.number])

# Load training feature names from scaler object (stored during training)
if hasattr(scaler, "feature_names_in_"):
    expected_features = scaler.feature_names_in_
else:
    raise ValueError("Scaler does not have saved feature names. Please retrain with scikit-learn >= 1.0")

# Align features: add missing columns, drop extras
for col in expected_features:
    if col not in X_new.columns:
        X_new[col] = 0  # Fill missing columns with 0
X_new = X_new[expected_features]  # Ensure correct column order

# Step 6: Scale and Predict
X_new_scaled = scaler.transform(X_new)
predictions = model.predict(X_new_scaled)
new_students["predicted_dropout"] = predictions

# Step 7: Save predictions
new_students.to_csv("predicted_dropouts.csv", index=False)
print("Predictions saved to predicted_dropouts.csv")
