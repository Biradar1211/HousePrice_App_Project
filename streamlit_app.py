import streamlit as st
import joblib
import pandas as pd
from config import collection  # MongoDB collection from config.py

# Load trained model and encoder
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")

# App UI
st.set_page_config(page_title="🏡 House Price Predictor", layout="centered")
st.title("🏡 House Price Predictor")
st.markdown("Enter the details below to predict the house price:")

# Input fields
area = st.number_input("Area (in sqft)", min_value=100, max_value=10000, step=50, value=1200)
rooms = st.number_input("Number of Rooms", min_value=1, max_value=10, value=3)
location = st.selectbox("Location", ["Hyderabad", "Mumbai", "Bangalore", "Chennai", "Delhi"])

if st.button("🔮 Predict"):
    # One-hot encode location
    location_encoded = encoder.transform([[location]]).toarray()[0]
    features = [area, rooms] + list(location_encoded)

    # Predict price
    predicted_price = model.predict([features])[0]
    st.success(f"💰 Estimated Price: ₹ {predicted_price:.2f} Lakhs")

    # Save to MongoDB
    record = {
        "area": area,
        "rooms": rooms,
        "location": location,
        "predicted_price": float(predicted_price)
    }
    collection.insert_one(record)
    st.info("Prediction saved to MongoDB ✅")
