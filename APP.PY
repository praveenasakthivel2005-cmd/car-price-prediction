import streamlit as st
import joblib
import pandas as pd 
import numpy as np
from sklearn.compose import ColumnTransformer

# Load model
model = joblib.load(r"C:\Users\Admin\Desktop\ML PROJECT\Car_Price_Prediction.joblib")
st.set_page_config(page_title="Car Price Predictor", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #ff4b4b;'>🚗 Car Price Prediction App</h1>",
    unsafe_allow_html=True
)

st.image(r"C:\Users\Admin\Desktop\ML PROJECT\AWS_Streamlit\Find your dream car today.png", use_container_width=True)

st.subheader("Enter Car Details")

# 🔹 Inputs (ALL ABOVE)
car_id = st.number_input("Car ID", 1, 10000, 1)
brand = st.selectbox("Brand", ["Toyota", "BMW", "Hyundai"], key="brand")
year = st.number_input("Year", 2000, 2024, 2018)
engine_size = st.number_input("Engine Size", 800, 5000, 1500)

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"], key="fuel")
transmission = st.selectbox("Transmission", ["Manual", "Automatic"], key="transmission")

mileage = st.number_input("Mileage", 10.0, 40.0, 20.0)
condition = st.selectbox("Condition", ["New", "Used"], key="condition")
model_name = st.text_input("Model", "Swift")


# 🔹 Button block (BELOW)
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        'Car ID': [car_id],
        'Brand': [brand],
        'Year': [year],
        'Engine Size': [engine_size],
        'Fuel Type': [fuel],
        'Transmission': [transmission],
        'Mileage': [mileage],
        'Condition': [condition],
        'Model': [model_name]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated Price: ₹ {prediction:.2f}")
