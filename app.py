import streamlit as st
import pickle
import numpy as np

# Load the trained model
import joblib

model = joblib.load("stroke_prediction_model.pkl")
st.set_page_config(page_title="Stroke Prediction System", page_icon="🩺")

st.title("🩺 Stroke Prediction System")
st.write("Enter the patient details below to predict the risk of stroke.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=120, value=25)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0)
bmi = st.number_input("BMI", min_value=0.0)

# Convert gender to numeric
gender = 1 if gender == "Male" else 0

# Prediction
if st.button("Predict"):

    input_data = np.array([[gender,
                            age,
                            hypertension,
                            heart_disease,
                            avg_glucose_level,
                            bmi]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠ High Risk of Stroke")
    else:
        st.success("✅ Low Risk of Stroke")
