import pandas as pd
import joblib

# Load models
clf = joblib.load("models/irrigation_model.pkl")
reg = joblib.load("models/waterlevel_model.pkl")

# Load encoders
soil_encoder = joblib.load("encoders/encoder_Soil_Type.pkl")
crop_encoder = joblib.load("encoders/encoder_Crop.pkl")
season_encoder = joblib.load("encoders/encoder_Season.pkl")

# Function to predict irrigation and water level
def predict_irrigation(input_data):
    # Encode categorical
    input_data["Soil_Type"] = soil_encoder.transform([input_data["Soil_Type"]])[0]
    input_data["Crop"] = crop_encoder.transform([input_data["Crop"]])[0]
    input_data["Season"] = season_encoder.transform([input_data["Season"]])[0]

    # Convert to DataFrame
    X_new = pd.DataFrame([input_data])

    # Predict
    irrigation_needed = clf.predict(X_new)[0]
    water_level = reg.predict(X_new)[0]

    print("Irrigation Needed:", "Yes" if irrigation_needed==1 else "No")
    print("Recommended Water Level:", round(water_level, 2), "liters")


# Example usage
input_data = {
    "Rainfall": 20,
    "Temperature": 32,
    "Humidity": 45,
    "Soil_Type": "Loamy",
    "Crop": "Wheat",
    "Season": "Rabi"
}

predict_irrigation(input_data)
