import streamlit as st

st.set_page_config(page_title="Smart Irrigation", page_icon="💧")

st.title("💧 SMART AGRI IRRIGATION DASHBOARD")
st.write("Provide environmental values to check if irrigation is needed and how much water to supply.")

# ----------------- INPUTS -----------------
soil_moisture = st.number_input("🌱 Soil Moisture (%)", 0, 100, 35)
temperature = st.number_input("🌡️ Temperature (°C)", 0, 60, 30)
humidity = st.number_input("💨 Humidity (%)", 0, 100, 45)
rainfall = st.number_input("🌧️ Rainfall (mm)", 0, 500, 10)

st.write("---")

# ----------------- PREDICTION BUTTON -----------------
if st.button("🔍 Predict Irrigation"):

    irrigation_needed = False
    water_litres = 0

    # ---------- Decision Logic ----------
    if soil_moisture < 40:
        irrigation_needed = True
    
    if rainfall > 60:
        irrigation_needed = False

    if temperature > 35 and humidity < 40:
        irrigation_needed = True

    # ---------- Water Calculation ----------
    if irrigation_needed:
        # Base litres logic
        deficit = max(0, 40 - soil_moisture)   # 40% ideal moisture
        water_litres = deficit * 10            # 1% deficit -> 10 litres

        # Temperature effect
        if temperature > 35:
            water_litres += 50
        elif temperature > 30:
            water_litres += 25

        # Rain compensation
        if rainfall > 20:
            water_litres -= 20
        
        water_litres = max(water_litres, 10)   # minimum water supply

    # ---------------- OUTPUT ----------------
    st.subheader("📌 Result")

    if irrigation_needed:
        st.success("🚜 Irrigation Needed")
        st.write(f"💧 Recommended Water Quantity: **{int(water_litres)} Litres**")
    else:
        st.info("✅ Irrigation NOT Needed")
        st.write("Soil and weather conditions are healthy. No watering required.")

    st.write("---")
    st.write("🧠 Decision based on:")
    st.write("- Soil moisture priority")
    st.write("- Rainfall impact")
    st.write("- Heat and humidity effect")
