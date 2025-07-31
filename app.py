import streamlit as st
import pandas as pd
import numpy as np
import joblib

# City coordinates for mapping
city_coords = {
    'Delhi': [28.6139, 77.2090],
    'Mumbai': [19.0760, 72.8777],
    'Chennai': [13.0827, 80.2707],
    'Kolkata': [22.5726, 88.3639],
    'Hyderabad': [17.3850, 78.4867],
    'Bangalore': [12.9716, 77.5946]
}

# Load trained model
model = joblib.load('model.pkl')

# ----------------- Streamlit UI ---------------------
st.set_page_config(page_title="Flight Price Predictor", page_icon="✈️", layout="centered")

st.title("✈️ Flight Price Predictor")
st.markdown("Predict the price of a domestic flight in India based on key details.")

# ------------------ Input Fields --------------------
st.subheader("📋 Enter Flight Details")

col1, col2 = st.columns(2)

with col1:
    airline = st.selectbox("✈️ Airline", ['SpiceJet', 'Vistara', 'AirAsia', 'Indigo'])
    source_city = st.selectbox("📍 Source City", list(city_coords.keys()))
    departure_time = st.selectbox("🕐 Departure Time", ['Morning', 'Evening', 'Early_Morning', 'Afternoon', 'Night', 'Late_Night'])
    stops = st.selectbox("🛑 Stops", ['zero', 'one', 'two_or_more'])

with col2:
    destination_city = st.selectbox("📍 Destination City", list(city_coords.keys()))
    arrival_time = st.selectbox("🕓 Arrival Time", ['Morning', 'Evening', 'Early_Morning', 'Afternoon', 'Night', 'Late_Night'])
    travel_class = st.selectbox("💺 Class", ['Economy', 'Business'])
    duration = st.number_input("⏱ Duration (in hours)", min_value=0.0, format="%.2f")
    days_left = st.slider("📆 Days Left Until Flight", 1, 60, 30)

# ------------------ Prediction ----------------------
st.subheader("💸 Predict Flight Price")

if st.button("Predict Price"):
    new_data = pd.DataFrame({
        'airline': [airline],
        'source_city': [source_city],
        'departure_time': [departure_time],
        'stops': [stops],
        'arrival_time': [arrival_time],
        'destination_city': [destination_city],
        'class': [travel_class],
        'duration': [duration],
        'days_left': [days_left]
    })

    predicted_price = model.predict(new_data)[0]
    st.success(f"🎯 Predicted Flight Price: ₹{predicted_price:,.2f}")

    # ------------------ Map Display ----------------------
    if source_city != destination_city:
        st.subheader("🗺️ Flight Route Map")
        map_df = pd.DataFrame([
            {"City": "Source", "lat": city_coords[source_city][0], "lon": city_coords[source_city][1]},
            {"City": "Destination", "lat": city_coords[destination_city][0], "lon": city_coords[destination_city][1]},
        ])
        st.map(map_df)

# ------------------ Footer ----------------------
st.markdown("---")
st.markdown("🔧 Built with Streamlit · 💼 Flight Price Prediction Model · 🇮🇳 India Domestic Routes")


