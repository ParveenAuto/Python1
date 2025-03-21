
# Step 1: Import Libraries
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from datetime import datetime

# Step 2: Load Dataset
df = pd.read_csv("/Users/pd/Desktop/python/RES4CITY_Project/RapidMinerOutput.csv")

# Step 3: Date Processing
df['enrolment-date'] = pd.to_datetime(df['enrolment-date'], errors='coerce')
df['date_joined'] = pd.to_datetime(df['date_joined'], errors='coerce')
df['date_earned'] = pd.to_datetime(df['date_earned'], errors='coerce')

# Step 4: Feature Engineering
df['days_to_enroll'] = (df['enrolment-date'] - df['date_joined']).dt.days
df['earned_flag'] = df['date_earned'].notna().astype(int)
df['week_enrolled'] = df['enrolment-date'].dt.weekday
df['joined_hour'] = pd.to_datetime(df['joined_time'], errors='coerce').dt.hour
df['days_since_enroll'] = (datetime.now() - df['enrolment-date']).dt.days
df.fillna({
    'days_to_enroll': df['days_to_enroll'].median(),
    'week_enrolled': df['week_enrolled'].mode()[0],
    'joined_hour': df['joined_hour'].mode()[0],
    'days_since_enroll': df['days_since_enroll'].median()
}, inplace=True)

# Step 5: Dropout Label (with controlled noise)
df['dropout'] = (
    (df['grade'].isna()) &
    (df['earned_flag'] == 0) &
    (df['modules_attempted'] <= 1) &
    (df['days_since_enroll'] > 30)
).astype(int)
np.random.seed(42)
flip_idx = np.random.choice(df.index, size=int(0.07 * len(df)), replace=False)
df.loc[flip_idx, 'dropout'] = 1 - df.loc[flip_idx, 'dropout']

# Step 6: Prepare Features
drop_cols = ['user_id', 'enrolment-date', 'date_joined', 'date_earned',
             'joined_time', 'enrolment_time', 'earned_time', 'grade']
X = df.drop(columns=drop_cols, errors='ignore').select_dtypes(include=[np.number])
y = df['dropout']

# Step 7: Train-Test Split and Scaling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
joblib.dump(scaler, "dropout_scaler.pkl")

# Step 8: Train and Save Models
models = {
    "random_forest": RandomForestClassifier(random_state=42),
    
    "xgboost": XGBClassifier(use_label_encoder=False, eval_metric='logloss')
}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    joblib.dump(model, f"model_{name}.pkl")
    y_pred = model.predict(X_test_scaled)
    print(f"Model: {name}")
    print("  Accuracy:", accuracy_score(y_test, y_pred))
    print("  Precision:", precision_score(y_test, y_pred))
    print("  Recall:", recall_score(y_test, y_pred))
    print("  F1 Score:", f1_score(y_test, y_pred))
    print("  ROC AUC:", roc_auc_score(y_test, y_pred))
    print()
