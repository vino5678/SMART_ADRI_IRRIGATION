import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import joblib
import os

# Load data from SQLite
conn = sqlite3.connect("database/irrigation.db")
df = pd.read_sql("SELECT * FROM sensor_data", conn)
conn.close()

# Encode categorical
os.makedirs("encoders", exist_ok=True)
os.makedirs("models", exist_ok=True)
for col in ["Soil_Type","Crop","Season"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    joblib.dump(le, f"encoders/encoder_{col}.pkl")

X = df[["Rainfall","Temperature","Humidity","Soil_Type","Crop","Season"]]
y_irrigation = df["Irrigation_Needed"] if "Irrigation_Needed" in df else df["Humidity"].apply(lambda x:1 if x<50 else 0)
y_water = df["Water_Level"] if "Water_Level" in df else df["Humidity"]*10

X_train, X_test, y_train, y_test = train_test_split(X, y_irrigation, test_size=0.2)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)
joblib.dump(clf, "models/irrigation_model.pkl")

reg = RandomForestRegressor(n_estimators=100)
reg.fit(X_train, y_water)
joblib.dump(reg, "models/waterlevel_model.pkl")
