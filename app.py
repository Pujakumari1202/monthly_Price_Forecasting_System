
import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title("📈 Monthly Price Forecasting System")

# Inputs
year = st.number_input("Enter Year", 2025, 2050, 2026)
month = st.slider("Select Month", 1, 12)

# Prediction
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        'Year': [year],
        'Month': [month]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Monthly Price: ₹ {prediction[0]:,.2f}"
    )
