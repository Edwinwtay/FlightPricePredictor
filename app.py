import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load('model.pkl')

# App title
st.title("✈️ Flight Price Predictor")

# User input
airline = st.selectbox("Airline", ['SpiceJet', 'Vistara', 'AirAsia', 'Indigo'])
source_city = st.selectbox("Source City", ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Hyderabad', 'Bangalore'])
departure_time = st.selectbox("Departure Time", ['Morning', 'Evening', 'Early_Morning', 'Afternoon', 'Night', 'Late_Night'])
stops = st.selectbox("Stops", ['zero', 'one', 'two_or_more'])
arrival_time = st.selectbox("Arrival Time", ['Morning', 'Evening', 'Early_Morning', 'Afternoon', 'Night', 'Late_Night'])
destination_city = st.selectbox("Destination City", ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Hyderabad', 'Bangalore'])
travel_class = st.selectbox("Class", ['Economy', 'Business'])
duration = st.number_input("Duration (in hours)", min_value=0.0, format="%.2f")
days_left = st.slider("Days Left Until Flight", 1, 60, 30)

# Predict
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
    st.success(f"✈️ Predicted Flight Price: ₹{predicted_price:,.2f}")


