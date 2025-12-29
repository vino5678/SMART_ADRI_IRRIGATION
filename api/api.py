# api/api.py
from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

clf = joblib.load("models/irrigation_model.pkl")
reg = joblib.load("models/waterlevel_model.pkl")
soil_encoder = joblib.load("encoders/encoder_Soil_Type.pkl")
crop_encoder = joblib.load("encoders/encoder_Crop.pkl")
season_encoder = joblib.load("encoders/encoder_Season.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    df["Soil_Type"] = soil_encoder.transform(df["Soil_Type"])
    df["Crop"] = crop_encoder.transform(df["Crop"])
    df["Season"] = season_encoder.transform(df["Season"])
    irrigation = clf.predict(df)[0]
    water = reg.predict(df)[0]
    return jsonify({"Irrigation_Needed": int(irrigation), "Water_Level": float(water)})

if __name__=="__main__":
    app.run(port=5000)
