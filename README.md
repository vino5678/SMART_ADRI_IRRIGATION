# SMART_AGRI_IRRIGATION

Smart Agriculture Irrigation System using IoT & Machine Learning

🌟 Project Overview

SMART_ADRI_IRRIGATION is an intelligent irrigation system designed to help farmers make accurate watering decisions. It collects environmental data such as soil moisture, temperature, humidity, and rainfall, and predicts whether irrigation is needed and the recommended water quantity.

⚡ Features

🌱 Simulates IoT sensors for soil and weather parameters

📊 Real-time data visualization using Streamlit Dashboard

🚜 Smart irrigation decision based on environmental conditions

💧 Calculates recommended water quantity in litres

🔗 Easy to extend with MQTT, SQLite, or Machine Learning models

📝 Inputs

🌱 Soil Moisture (%)

🌡️ Temperature (°C)

💨 Humidity (%)

🌧️ Rainfall (mm)

🏆 Outputs

✅ Irrigation Status: Yes / No

💧 Recommended Water Quantity (Litres)

🧠 Model & Working
How It Works

The system predicts irrigation based on the inputs:

Soil Moisture

Temperature

Humidity

Rainfall

Rule-based Decision Logic Example:

Soil moisture < 40% → irrigation needed

Rainfall > 60mm → no irrigation

High temperature + low humidity → irrigation needed

Water quantity is calculated from soil moisture deficit and heat effect

How to Use

Run the Streamlit Dashboard:

streamlit run dashboard/app.py


Enter the environmental values.

Click Predict Irrigation.

View:

🌿 Irrigation Needed / Not Needed

💧 Recommended Water Quantity

Optional ML Integration

Replace rule-based logic with a trained ML model (RandomForest / DecisionTree)

Train on historical sensor data to improve predictions

Save the model as irrigation_model.pkl and load in dashboard or API

🛠️ Technologies Used

🐍 Python 3

📊 Streamlit

🔗 Git & GitHub

⚡ Optional: MQTT, SQLite, Scikit-learn

🚀 How to Run

Clone the repository:

git clone https://github.com/vino5678/SMART_ADRI_IRRIGATION.git


Navigate to project folder:

cd SMART_ADRI_IRRIGATION/dashboard


Install requirements:

pip install -r requirements.txt


Run Streamlit dashboard:

streamlit run app.py


Enter input values and check irrigation status & water quantity.

📂 Project Structure
SMART_ADRI_IRRIGATION/
│
├─ dashboard/        # Streamlit dashboard code
│   └─ app.py
├─ ml/               # Machine learning model (optional)
├─ sensors/          # Sensor simulator code (optional)
├─ api/              # Flask REST API (optional)
├─ requirements.txt
└─ README.md

✅ Benefits

Helps farmers make data-driven irrigation decisions

Reduces water wastage 💧

Can be extended to real-time IoT sensors 🌿
