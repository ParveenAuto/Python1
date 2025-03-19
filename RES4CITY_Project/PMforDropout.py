# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import joblib

# Step 2: Load the Cleaned Dataset
file_path = "/Users/pd/Desktop/python/RES4CITY_Project/RapidMinerOutput.csv"
df = pd.read_csv(file_path)

# Step 3: Convert `grade` from percentage string to float
df['grade'] = df['grade'].str.replace('%', '', regex=True).astype(float)

# Step 4: Feature Engineering
# Convert dates to datetime format
df['enrolment-date'] = pd.to_datetime(df['enrolment-date'], errors='coerce')
df['date_joined'] = pd.to_datetime(df['date_joined'], errors='coerce')

# Calculate days since enrollment and days since joining
df['days_since_enrollment'] = (pd.to_datetime("today") - df['enrolment-date']).dt.days
df['days_since_joined'] = (pd.to_datetime("today") - df['date_joined']).dt.days

# Fill missing values with median
df['days_since_enrollment'].fillna(df['days_since_enrollment'].median(), inplace=True)
df['days_since_joined'].fillna(df['days_since_joined'].median(), inplace=True)

# Step 5: More Realistic Dropout Calculation
# Set minimum engagement period before marking dropout risk
DEFAULT_MIN_ENGAGEMENT_DAYS = 14  # 2 weeks
DEFAULT_MAX_COMPLETION_DAYS = 30  # 1 month

# If module duration is available, use that (otherwise, default to 14 days)
if 'avg_module_duration' in df.columns:
    df['min_engagement_days'] = df['avg_module_duration'].fillna(DEFAULT_MIN_ENGAGEMENT_DAYS)
    df['max_completion_days'] = df['avg_module_duration'] * 2
else:
    df['min_engagement_days'] = DEFAULT_MIN_ENGAGEMENT_DAYS
    df['max_completion_days'] = DEFAULT_MAX_COMPLETION_DAYS

# Define dropout conditions (less strict than before)
df["dropout"] = np.where(
    ((df["days_since_enrollment"] > df['min_engagement_days']) & (df["modules_attempted"] == 0)) |  # No modules in 2 weeks
    ((df["days_since_joined"] > df['max_completion_days']) & (df["modules_attempted"] == 0)) |  # No modules in 1 month
    ((df["days_since_joined"] > df['max_completion_days']) & (df["grade"] == 0)),  # Grade 0 after reasonable time
    1,  # High dropout risk
    0   # Not a dropout
)

# Step 6: Define Features & Target Variable
X = df.drop(columns=['user_id', 'enrolment-date', 'date_joined', 'date_earned', 'dropout', 'min_engagement_days', 'max_completion_days'], errors='ignore')
y = df["dropout"]

# Step 7: Train-Test Split (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Step 8: Balance the Dataset with SMOTE (Fix Class Imbalance)
smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
import joblib
joblib.dump(X_train.columns.tolist(), "model_features.pkl")
# Standardize numerical features (only for Logistic Regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_balanced)
X_test_scaled = scaler.transform(X_test)

# Step 9: Train Machine Learning Models with Regularization
xgb = XGBClassifier(
    eval_metric="logloss", 
    max_depth=4,  # Reduce depth to prevent overfitting
    learning_rate=0.05,  
    n_estimators=150,  
    reg_lambda=2.0,  
    subsample=0.8,  
    colsample_bytree=0.8,  
    random_state=42
)
rf = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)

# Train Models Again
rf.fit(X_train_balanced, y_train_balanced)
xgb.fit(X_train_balanced, y_train_balanced)

# Step 10: Evaluate Model Performance
def evaluate_model(y_test, y_pred, model_name):
    print(f"\n--- {model_name} Model Evaluation ---")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print(f"Precision: {precision_score(y_test, y_pred):.2f}")
    print(f"Recall: {recall_score(y_test, y_pred):.2f}")
    print(f"F1 Score: {f1_score(y_test, y_pred):.2f}")
    print(f"ROC AUC Score: {roc_auc_score(y_test, y_pred):.2f}")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")

# Evaluate all models
y_pred_rf = rf.predict(X_test)
y_pred_xgb = xgb.predict(X_test)
evaluate_model(y_test, y_pred_rf, "Random Forest")
evaluate_model(y_test, y_pred_xgb, "XGBoost")

# Step 11: Cross-Validation for Model Stability
cv_scores = cross_val_score(xgb, X_train_balanced, y_train_balanced, cv=5, scoring="accuracy")
print(f"\nCross-Validation Accuracy: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

# Step 12: Save the Trained Model for Future Predictions
joblib.dump(xgb, "dropout_prediction_model.pkl")
print("Model saved successfully!")