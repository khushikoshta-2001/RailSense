import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("dt_model.pkl")

st.title("🚆 RailSense")
st.subheader("Smart Passenger Boarding Predictor for Indian Railways")
st.write("Enter journey details to predict if a passenger may not show up.")

# ---- INPUTS ----
distance_km = st.number_input("Distance (km)", 0.0, 2000.0, 100.0)
delay_minutes = st.number_input("Delay (minutes)", 0.0, 500.0, 30.0)
departure_hour = st.slider("Departure Hour", 0, 23, 10)

zone_congestion = st.slider("Zone Congestion Index", 0.0, 1.0, 0.5)
seat_utilisation = st.slider("Seat Utilisation (%)", 0.0, 100.0, 70.0)

is_weekend = st.selectbox("Weekend?", [0, 1])
is_peak_hour = st.selectbox("Peak Hour?",[0, 1])
is_night = st.selectbox("Night Departure?",[0, 1])

# ---- FEATURE VECTOR (VERY IMPORTANT: SAME ORDER AS TRAINING) ----
features = np.array([[
    distance_km,
    delay_minutes,
    departure_hour,
    zone_congestion,
    seat_utilisation,
    is_weekend,
    is_peak_hour,
    is_night,
    0,  # is_monsoon_season
    0,  # is_fog_risk
    0,  # is_overloaded
    0,  # late_incoming_rake
    0,  # train_type_idx
    0,  # Quota_idx
    0,  # Class of Travel_idx
    0   # Booking Channel_idx
]])

# ---- PREDICTION ----
if st.button("Predict"):
    prob = model.predict_proba(features)[0][1]

    st.subheader(f"📊 No-Show Probability: {prob:.2f}")

    if prob > 0.5:
        st.error("⚠️ High chance of no-show")
    else:
        st.success("✅ Likely to travel")

    # ---- SIMPLE EXPLANATION ----
    if delay_minutes > 60 and distance_km < 200:
        st.info("💡 High delay + short distance increases no-show risk")
